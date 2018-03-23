from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'home.html')


def add_test(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add_test_two(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


# 利用reverse逆向解析url 也不知道写的对不对
def add_test_three(request, a, b):
    reverse('add3', args=(a, b))
    c = int(a) + int(b)
    return HttpResponse(str(c))


def home_page(request):
    string = u'试一试使用{{}}来导入字符串'
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home_page.html', {'TutorialList': TutorialList})

