from django.http import HttpResponse
from django.shortcuts import render
import operator
from.import count


def home(request):
    return render(request, 'home.html', {'key': 'Hi im from python ,we ace use pthon inline also '})


def about(request):
    return render(request, 'about.html')


def result(request):
    name = request.GET['user_name']
    age = request.GET['user_age']
    message = f'HI ,{name},you are {age} years'
    article = request.GET['article']
    word_count, var_dict = count.count(article)  # this is the system to call the .py module
    return render(request, 'result.html', {'age': message, 'article': article, 'word_count': word_count, 'dict_words': var_dict })
