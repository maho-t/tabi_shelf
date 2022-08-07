from django.urls import path
from . import views

urlpatterns = [
  path('', TabiList.as_views(), name='list'),
]