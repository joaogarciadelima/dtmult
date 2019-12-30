from django.urls import path

from dtmult.propriedades.views import indice, propriedade

app_name = 'propriedades'
urlpatterns = [
    path('<slug:slug>', propriedade, name='propriedade'),
    path('', indice, name='indice'),
]
