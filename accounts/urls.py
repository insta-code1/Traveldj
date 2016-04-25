from django.conf.urls import url
from accounts.views import *

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='logout'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^profile/$', profile, name='profile'),
]