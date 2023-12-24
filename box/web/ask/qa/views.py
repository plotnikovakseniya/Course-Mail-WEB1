from django import forms
from django.contrib.auth.forms import UserCreationForm
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.db.models.functions import Now

# форма регистрации нового пользователя
class SignupForm(UserCreationForm):
  email = forms.EmailField # почта

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']


# форма авторизации - встроенная (AuthenticationForm)



# форма добавления вопроса
class AskForm(forms.Form):
  title = forms.CharField(max_length=100) # поле заголовка
  text = forms.CharField(widget=forms.Textarea) # поле текста вопроса

  class Meta:
    model = Question
    fields = ['title', 'text']

  def clean_title(self):
    title = self.cleaned_data['title']
    if title.isspace():
      raise forms.ValidationError(u'Заголовок не должен быть пустым', code=1)
    return title

  def clean_text(self):
    text = self.cleaned_data['text']
    if text.isspace():
      raise forms.ValidationError(u'Текст вопроса не должен быть пустым', code=1)
    return text

  def save(self):
    question = Question(title=self.cleaned_data['title'],
      text=self.cleaned_data['text'],
      rating=0,
      author=self.author,
      added_at=Now())
    question.save()
    return question


# форма добавления ответа
class AnswerForm(forms.Form):
  text = forms.CharField(widget=forms.Textarea) # поле текста ответа
  question = 0 # поле для связи с вопросом

  class Meta:
    model = Answer
    fields = ['text']

  def clean_text(self):
    text = self.cleaned_data['text']
    if text.isspace():
      raise forms.ValidationError(u'Поля текста вопроса и ответа не должны быть пустыми', code=2)
    return text

  def save(self):
    answer = Answer(text=self.cleaned_data['text'],
      added_at=Now(),
      author=self.author,
      question=self.question)
    answer.save()
    return answer
