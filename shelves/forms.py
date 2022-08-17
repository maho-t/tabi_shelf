from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from .models import Tabi

class TabiModelForm(forms.ModelForm):
  date = forms.DateField(
    label = '日付',
    widget=DatePickerInput(format='%Y-%m-%d')
  )

class TabiModelForm(forms.ModelForm):
  genre = forms.fields.ChoiceField(
    choice_genre = (
      ('1', '体験／教室'),
      ('2', 'スポーツ／観戦'),
      ('3', '自然／景色／花'),
      ('4', '動物'),
      ('5', '宿泊'),
      ('6', 'グルメ'),
      ('7', '文化／芸術'),
      ('8', '祭り'),
      ('9', 'テーマパーク'),
      ('10', 'ショッピング'),
      ('11', '世界遺産／遺産'),
      ('12', '乗り物'),
      ('13', 'スパ／エステ／温泉'),
      ('14', '学習／研修'),
      ('15', 'その他')
    ),
    required=True,
    widget=forms.widgets.Select
  )