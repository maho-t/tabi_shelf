from django.urls import path
from .views import TabiList

urlpatterns = [
  path('', TabiList.as_view(), name='list'),
]