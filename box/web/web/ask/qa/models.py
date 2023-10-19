from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
  def new(self):
    pass
  def popular(self):
    pass

class Question(models.Model):
  title = models.CharField(max_length=255)
  text = models.TextField()
  added_at = models.DateTimeField(blank=True)
  rating = models.IntegerField()
  author = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='author')
  likes = models.ManyToManyField(User, related_name='likes')
  objects = QuestionManager()

class Answer(models.Model):
  text = models.TextField()
  added_at = models.TextField()
  question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
  author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
