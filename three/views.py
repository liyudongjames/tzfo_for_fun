from django.shortcuts import render
from django.http import HttpResponse


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
