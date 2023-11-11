from django.http import HttpResponse
from django.shortcuts import render

def about(req):
    return HttpResponse('Салам алейкум')

def home(req):
    return render(req, 'home.html', {'greeting': 'Hello'})