from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Tabi

class TabiList(ListView):
  model = Tabi
  context_object_name = "journeys"

class TabiDetail(DetailView):
  model = Tabi
  context_object_name = "journey"