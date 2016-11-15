from django.conf.urls import url

from l4f.views import HomePageView, get_channel_history

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home_page'),
    url(r'^history', get_channel_history, name='get_history'),
]
