from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('question_detail/<int:id>/',
         views.question_detail, name='question_detail'),
    path('question_ask/', views.question_ask, name='question_ask'),
    path('question_detail/<int:id>/edit',
         views.question_edit, name='question_edit'),
    path('question/<int:id>/delete', views.question_delete, name='question_delete'),
    path('answer/<int:id>/edit', views.answer_edit, name='answer_edit'),
    path('answer/<int:id>/delete', views.answer_delete, name='answer_delete'),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]
