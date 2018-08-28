"""tzfo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from three import views as three_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', three_view.index),
    path('add/', three_view.add_test),
    path('add_person/', three_view.add_person),
    path('add/<int:a>/<int:b>/', three_view.add_test_two, name='add'),
    path('new_add/<int:a>/<int:b>/', three_view.add_test_two, name='add2'),
    path('newed_add/<int:a>/<int:b>/', three_view.add_test_three, name='add3'),
    path('get_person', three_view.get_person),
    path('home_page/', three_view.home_page),
    path('append/', three_view.test_get),
    path('multiply/', three_view.multiply_practice, name='multiply'),
    path('form_post/', three_view.form_practice),
    path('testing_for_css', three_view.testing_css),
    path('testing_for_video', three_view.testing_video),
    path('div_demo', three_view.testing_div),
    path('information_test', three_view.testing_information),
]
