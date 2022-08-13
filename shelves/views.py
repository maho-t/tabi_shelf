import imp
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from django.urls import reverse_lazy

from .models import Tabi

class TabiList(ListView):
  model = Tabi
  context_object_name = "journeys"

class TabiDetail(DetailView):
  model = Tabi
  context_object_name = "journey"

class TabiCreate(CreateView):
  model = Tabi
  fields = "__all__"
  success_url = reverse_lazy('list')