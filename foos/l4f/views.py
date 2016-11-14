from django.http import HttpResponse

from slacker import Slacker

slack = Slacker('* slack token here*')
channel = '#l4f'


def index(request):
    slack_string = 'This is a test... 123...'
    slack.chat.post_message(channel, slack_string)
    return HttpResponse("Put foose stuff here")
