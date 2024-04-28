from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio' ),
    path('calculando', views.index, name='index' ),
    path('imc', views.imc, name='imc' )
]
