from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-home'),
    path('processScheduling', views.ps, name='home-processScheduling'),
]
