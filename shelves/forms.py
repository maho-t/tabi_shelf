from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import Tabi

class TabiForm(forms.ModelForm):
  class Meta:
    model = Tabi
    fields = ['title', 'date', 'place', 'genre', 'accompany', 'text']
    widget = {'date': DatePickerInput(),}