from django.urls import path
from . import views

urlpatterns = [
  path('manager/', views.show_list, name='manage')
]