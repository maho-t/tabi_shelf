from cgitb import text
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Tabi
from . import forms

class TabiList(ListView):
  model = Tabi
  context_object_name = "journeys"

  def get_queryset(self):
    queryset = Tabi.objects.order_by('-created_date')
    query = self.request.GET.get('query')

    if query:
      queryset = queryset.filter(
      Q(title__icontains=query) | Q(text__icontains=query)
      )
    return queryset

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