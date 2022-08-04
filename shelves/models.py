from tabnanny import verbose
from turtle import mode
from django.db import models

class Tabi(models.Model):
  title = models.CharField(max_length=30)
  date = models.DateField
  place = models.CharField(verbose_name='PLACE', max_length=20)
  genre = models.CharField(verbose_name='GENRE', max_length=40)
  accompany = models.CharField(verbose_name='PEOPLE', max_length=10)
  text = models.TextField

  class Meta:
    verbose_name_plural = 'Tabi_data'

  def __str__(self):
    return self.title