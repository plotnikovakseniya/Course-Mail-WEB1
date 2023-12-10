from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User
from django.forms import ModelForm


class QuestionManager(models.Manager):
  def new(self):
    return self.order_by('-added_at')
  def popular(self):
    return self.annotate(num_likes=Count('likes')).order_by('-num_likes')


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


class AskForm(ModelForm):
  class Meta:
    model = Question
    fields = ['title', 'text']


class AnswerForm(ModelForm):
  class Meta:
    model = Answer
    fields = ['text']

