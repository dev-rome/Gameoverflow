from django.shortcuts import render
from .models import Question, Answer

# Create your views here.
def index(request):
    return render(request, 'gameoverflow/index.html')

def question_list(request):
    questions = Question.objects.all()
    return render(request, 'gameoverflow/question_list.html', {'questions': questions})    