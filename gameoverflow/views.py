from urllib import request
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views import View
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

# Create your views here.


def index(request):
    return render(request, 'gameoverflow/index.html')


def question_list(request):
    questions = Question.objects.all()
    return render(request, 'gameoverflow/question_list.html', {'questions': questions})


def question_detail(request, pk):
    question = Question.objects.get(pk=pk)
    return render(request, 'gameoverflow/question_detail.html', {'question': question})


@login_required
def question_ask(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('question_detail', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'gameoverflow/question_ask.html', {'form': form})


class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, 'registration/signup.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('question_list')
        else:
            context = {"form": form}
            return render(request, 'registration/signup.html', context)
