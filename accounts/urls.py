from django.urls import URLPattern, path, include
from . import views

app_name = 'accounts'
ulrpatterns = [
  path('', include('django.contrib.auth.urls')),
  path('register/', views.register, name='register'),
]