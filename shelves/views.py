from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.urls import reverse_lazy

from .models import Tabi
from . import forms

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
  def get_form(self):
    form = super().get_form()
    form.fields['date'].widget = DateTimePickerInput(format='%Y-%m-%d')
    return form

class TabiUpdate(UpdateView):
  model = Tabi
  fields = "__all__"
  success_url = reverse_lazy('list')

class TabiDelete(DeleteView):
  model = Tabi
  context_object_name = "journey"
  success_url = reverse_lazy('list')