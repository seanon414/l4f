import os

from django.http import HttpResponse

from slacker import Slacker

slack_key = os.environ['SLACK_BOT']
slack = Slacker(slack_key)
channel = '#l4f'


def index(request):
    slack_string = 'This is a test... 123...'
    slack.chat.post_message(channel, slack_string)
    return HttpResponse('')
