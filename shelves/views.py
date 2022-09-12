from cgitb import text
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Tabi
from . import forms

class TabiList(LoginRequiredMixin, ListView):
  model = Tabi
  context_object_name = "journeys"

  def get_queryset(self):
    queryset = Tabi.objects.order_by('date')
    query = self.request.GET.get('query')

    if query:
      queryset = queryset.filter(
      Q(title__icontains=query) | Q(text__icontains=query)
      )
    return queryset

class TabiDetail(LoginRequiredMixin, DetailView):
  model = Tabi
  context_object_name = "journey"

class TabiCreate(LoginRequiredMixin, CreateView):
  model = Tabi
  fields = "__all__"
  success_url = reverse_lazy('list')
  def get_form(self):
    form = super().get_form()
    form.fields['date'].widget = DateTimePickerInput(format='%Y-%m-%d')
    return form

class TabiUpdate(LoginRequiredMixin, UpdateView):
  model = Tabi
  fields = "__all__"
  success_url = reverse_lazy('list')

class TabiDelete(LoginRequiredMixin, DeleteView):
  model = Tabi
  context_object_name = "journey"
  success_url = reverse_lazy('list')