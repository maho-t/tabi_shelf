from django.urls import path
from .views import TabiDetail, TabiList, TabiCreate, TabiUpdate

urlpatterns = [
  path('', TabiList.as_view(), name='list'),
  path('detail/<int:pk>', TabiDetail.as_view(), name='detail'),
  path('create/', TabiCreate.as_view(), name='create'),
  path('update/<int:pk>', TabiUpdate.as_view(), name='update'),
]