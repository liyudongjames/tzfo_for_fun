from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .forms import AddForm
from three.models import Person
from django.core import serializers


# Create your views here.
def index(request):
    return render(request, 'home.html')


def add_test(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b) + 10
    return HttpResponse(str(c))


def add_test_two(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


# 利用reverse逆向解析url 也不知道写的对不对
def add_test_three(request, a, b):
    reverse('add3', args=(a, b))
    c = int(a) + int(b)
    return HttpResponse(str(c))


def multiply_practice(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) * int(b)
    return HttpResponse(str(c))


def home_page(request):
    string = u'试一试使用{{}}来导入字符串'
    tutorial_list = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'string': string, 'TutorialList': tutorial_list}
    return render(request, 'home_page.html', {'info_dict': info_dict})


def test_get(request):
    return render(request, 'firstAppend.html')


def form_practice(request):
    if request.method == 'POST':
        form = AddForm(request.POST)

        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'form_add.html', {'form': form})


def testing_css(request):
    return render(request, 'testing_css.html')


def testing_video(request):
    return render(request, 'video_test.html')


def testing_div(request):
    return render(request, 'div_demo.html')


def testing_information(request):
    return render(request, 'information_test.html')


def get_person(request):
    data = serializers.serialize("json", Person.objects.all())
    return HttpResponse(str(data))


def add_person(request):
    name = request.GET.get('name', '')
    age = request.GET.get('age', 0)
    Person.objects.create(name=name, age=age)
    return HttpResponse(str('添加成功'))

