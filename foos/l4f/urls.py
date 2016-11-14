from django.conf.urls import url

from l4f.views import HomePageView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home_page'),
]
