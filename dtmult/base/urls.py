from django.urls import path

from dtmult.base.views import home

app_name = 'base'
urlpatterns = [
    path('', home, name='home')
]
