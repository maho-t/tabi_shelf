from django.db import models

class Tabi(models.Model):
  GENRE = (
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
    ('15', 'その他'),
  )

  ACCOMPANY = (
    ('A', '単独'),
    ('B', '友人'),
    ('C', '恋人'),
    ('D', '家族'),
    ('E', '仕事関係者'),
    ('F', '趣味仲間'),
    ('G', 'その他'),
  )

  title = models.CharField(verbose_name='旅タイトル', max_length=30)
  date = models.DateField(verbose_name='日付', auto_now=False)
  place = models.CharField(verbose_name='場所', max_length=20)
  genre = models.CharField(verbose_name='ジャンル', choices=GENRE, max_length=40)
  accompany = models.CharField(verbose_name='同行者', choices=ACCOMPANY, max_length=10)
  text = models.TextField(verbose_name='メモ')

  class Meta:
    verbose_name_plural = 'Tabi_data'

  def __str__(self):
    return self.title