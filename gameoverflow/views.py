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


def question_detail(request, id):
    question = Question.objects.get(pk=id)
    answers = Answer.objects.filter(question=question)
    answerform = AnswerForm()
    if request.method == 'POST':
        answerData = AnswerForm(request.POST)
        if answerData.is_valid():
            answer = answerData.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.save()
            return redirect('question_detail', id=answer.question.id)
    return render(request, 'gameoverflow/question_detail.html', {'question': question, 'answers': answers, 'answerform': answerform})


def question_edit(request, id):
    question = Question.objects.get(pk=id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('question_detail', id=question.id)
    else:
        form = QuestionForm(instance=question)
    return render(request, 'gameoverflow/question_form.html', {'form': form})


def answer_edit(request, id):
    answer = Answer.objects.get(pk=id)
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.save()
            return redirect('question_detail', id=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    return render(request, 'gameoverflow/answer_form.html', {'form': form})


def question_delete(request, id):
    Question.objects.get(pk=id).delete()
    return redirect('question_list')

# delete answer on question detail page


def answer_delete(request, id):
    answer = Answer.objects.get(pk=id)
    answer_id = answer.question.id
    answer.delete()
    return redirect('question_detail', id=answer_id)


@login_required
def question_ask(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('question_detail', id=question.id)
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
