import os

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
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            # Post to room if form is valid
            slack_string = 'This is a test... 123...'
            return HttpResponse(slack_string)
        else:
            return self.form_invalid(form, **kwargs)

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)
