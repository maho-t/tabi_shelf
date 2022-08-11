from django.shortcuts import render
from django.views.generic import ListView

from .models import Tabi

class TabiList(ListView):
  model = Tabi
  context_object_name = "journeys"