"""SHelper_scholarship URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('user', include('accounts.urls')),
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('notice/', views.notice, name='notice'),
    path('manage/', views.manage, name='manage'),
    path('about/', views.about, name='about'),
    path('result/', views.result, name='result'),
    path('calendar/', views.calendar, name='calendar'),
    path('result_contest/', views.result_contest, name='result_contest'),
    path('register/', views.register, name='register'),
    path('contest1/', views.contest1, name='contest1'),
    path('contest2/', views.contest2, name='contest2'),
    path('contest3/', views.contest3, name='contest3'),
    path('contest4/', views.contest4, name='contest4'),
    path('service1/', views.service1, name='service1'),
    path('service2/', views.service2, name='service2'),
    path('service3/', views.service3, name='service3'),
    path('service4/', views.service4, name='service4'),
    path('need_login/', views.need_login, name='need_login'),
    path('already/', views.already, name='already'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('is_admin/', views.is_admin, name='is_admin'),
    path('notice_result', views.notice_result, name='notice_result'),
    path('form/', views.form, name='form'),
    path('mypage/', views.mypage, name='mypage'),
    #url pattern 앞에 index/ 이거 붙는 애들 처리해줘야함
    #url regular regex check
]