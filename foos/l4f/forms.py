from django import forms
from django.forms.fields import IntegerField


class HomePageForm(forms.Form):
    number_of_players = IntegerField(required=False,
                                     initial=0,
                                     min_value=0,
                                     widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        super(HomePageForm, self).__init__(*args, **kwargs)
