from django.db import models

class Tabi(models.Model):
  title = models.CharField(verbose_name='旅タイトル', max_length=30)
  date = models.DateField(verbose_name='日付', auto_now=False)
  place = models.CharField(verbose_name='場所', max_length=20)
  genre = models.CharField(verbose_name='ジャンル', max_length=40)
  accompany = models.CharField(verbose_name='同行者', max_length=10)
  text = models.TextField(verbose_name='メモ')

  class Meta:
    verbose_name_plural = 'Tabi_data'

  def __str__(self):
    return self.title