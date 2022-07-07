from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question_list/', views.question_list, name='question_list'),
    path('question_detail/<int:id>/', views.question_detail, name='question_detail'),
    path('question_ask/', views.question_ask, name='question_ask'),
    # path('question/<int:pk>/edit/', views.question_edit, name='question_edit'),
    # path('question/<int:pk>/delete/', views.question_delete, name='question_delete'),
    # path('answer/<int:pk>/edit/', views.answer_edit, name='answer_edit'),
    # path('answer/<int:pk>/delete/', views.answer_delete, name='answer_delete'),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
]