from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput
from .models import Tabi

class TabiModelForm(forms.ModelForm):
  date = forms.DateField(
    label = '日付',
    widget=DatePickerInput(format='%Y-%m-%d')
  )