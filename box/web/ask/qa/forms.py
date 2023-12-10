from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.db.models.functions import Now

# форма добавления вопроса
class AskForm(forms.Form):
  title = forms.CharField(max_length=100) # поле заголовка
  text = forms.CharField(widget=forms.Textarea) # поле текста вопроса
  def clean_title(self):
    title = self.cleaned_data['title']
    if title.isspace():
      raise forms.ValidationErrror(u'Заголовок не должен быть пустым', code=1)
    return title
  def clean_text(self):
    text = self.cleaned_data['text']
    if text.isspace():
      raise forms.ValidationErrror(u'Текст вопроса не должен быть пустым', code=1)
    return text
  def save(self):
    question = Question(title=self.cleaned_data['title'],
      text=self.cleaned_data['text'],
      rating=0,
      author=User.objects.all()[:1].get(),
      added_at=Now())
    question.save()
    return question


# форма добавления ответа
class AnswerForm(forms.Form):
  text = forms.CharField(widget=forms.Textarea) # поле текста ответа
  question = 0 # поле для связи с вопросом

  def clean_text(self):
    text = self.cleaned_data['text']
    if text.isspace():
      raise forms.ValidationError(u'Поля текста вопроса и ответа не должны быть пустыми', code=2)
    return text

  def save(self):
    answer = Answer(text=self.cleaned_data['text'],
      added_at=Now(),
      author=User.objects.all()[:1].get(),
      question=self.question)
    answer.save()
    return answer
