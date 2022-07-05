from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from .models import Question, Answer

# Create your views here.
def index(request):
    return render(request, 'gameoverflow/index.html')

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'gameoverflow/question_list.html', {'questions': questions})

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
            return redirect('index')
        else:
            context = {"form": form}
            return render(request, 'registration/signup.html', context)        