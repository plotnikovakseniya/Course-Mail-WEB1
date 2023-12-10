from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import resolve
from django.core.paginator import Paginator
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm
from django.views.decorators.http import require_GET

# paginator.baseurl

def application(request, *args, **kwargs):
    current_url = resolve(request.path_info).url_name
    # /popular/?page=3 - список популярных вопросов
    # /?page=2 - главная страница со списком новых вопросов
    if current_url == 'main' or current_url == 'popular':
        return page_paginator(request, *args, **kwargs)
    elif current_url == 'question': # /question/5/ - страница одного вопроса
        return page_question(request, *args, **kwargs)
    elif current_url == 'ask': # /ask/ - страница для добавления вопрос
        return page_ask(request, *args, **kwargs)
    return HttpResponse('OK')


def page_ask(request, *args, **kwargs):
  if request.method == 'GET':
    form = AskForm()
  elif request.method == 'POST':
    form = AskForm(request.POST)
    if form.is_valid():
      try:
        question = form.save()
        question_url = '/question/' + str(question.id)
      except ValueError:
        raise Http404
      return HttpResponseRedirect(question_url)
  return render(request, 'ask.html', {
    'form': form
  })


@require_GET
def page_paginator(request, *args, **kwargs):
    current_url = resolve(request.path_info).url_name
    if current_url == 'main':
        questions = Question.objects.new()
    elif current_url == 'popular':
        questions = Question.objects.popular()
    try:
        page = request.GET.get('page', request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, 10)
    if current_url == 'main':
        paginator.baseurl = '/?page='
    elif current_url == 'popular':
        paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request, 'paginator.html', {
       'questions': page.object_list,
       'paginator': paginator, 'page': page,
    })


def page_question(request, *args, **kwargs):
    question = get_object_or_404(Question, pk=kwargs['pk'])
    answers = Answer.objects.filter(question__pk=kwargs['pk']).all()
    if request.method == 'GET':
      form = AnswerForm()
    elif request.method == 'POST':
      form = AnswerForm(request.POST)
      form.question = question
      if form.is_valid():
        answer = form.save()
        current_url = request.path_info
        return HttpResponseRedirect(current_url)
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
        'form': form
    })
