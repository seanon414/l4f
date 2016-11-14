from django import forms
from django.forms.fields import IntegerField


class HomePageForm(forms.Form):
    number_of_players = IntegerField(required=False,
                                     initial=1,
                                     min_value=1,
                                     max_value=3)

    def __init__(self, *args, **kwargs):
        super(HomePageForm, self).__init__(*args, **kwargs)
