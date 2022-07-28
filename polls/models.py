from datetime import timedelta
from django.utils import timezone
from django.db import models

class Question(models.Model):
  # id: There's not need to create an id attribute because Djando creates it by default.
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField("date published")

  def __str__(self):
    return self.question_text

  def was_published_recently(self):
    return self.pub_date >= timezone.now() - timedelta(days=1)

class Choice(models.Model):
  # id: There's not need to create an id attribute because Djando creates it by default.
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text
