import os

import simplejson as json
from django.http import HttpResponse
from django.views.generic import FormView
from slacker import Slacker

from l4f.forms import HomePageForm


slack_key = os.environ['SLACK_BOT']
slack = Slacker(slack_key)
channel = '#l4f'


class HomePageView(FormView):
    template_name = "templates/index.html"
    form_class = HomePageForm
    success_url = '/l4f'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            # Post to room if form is valid
            players = form.cleaned_data['number_of_players']
            slack_string = 'Looking for {} foos player(s)'.format(players)
            slack.chat.post_message(channel, slack_string)
            return self.form_valid(form, **kwargs)
        else:
            return self.form_invalid(form, **kwargs)

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


def get_channel_history(request):
    channel_id = slack.channels.get_channel_id('l4f')
    channel = slack.channels.history(channel_id, count=5)
    channel_history = channel.body['messages']
    return HttpResponse(json.dumps({'messages': channel_history}), content_type='application/json')
