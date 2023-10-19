from django.shortcuts import render
from django.http import HttpResponse 

def application(request, *args, **kwargs):
    return HttpResponse('OK')
