from django.urls import path
from .views import TabiDetail, TabiList

urlpatterns = [
  path('', TabiList.as_view(), name='list'),
  path('detail/<int:pk>', TabiDetail.as_view(), name='detail'),
]