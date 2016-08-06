from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.CheckUser, name='check User'),
    url(r'^feature$', views.CheckFeatures, name='check feature')
]
