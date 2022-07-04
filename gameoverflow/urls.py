from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question_list/', views.question_list, name='question_list'),
]