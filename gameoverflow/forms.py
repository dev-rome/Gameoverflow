from django import forms
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_title', 'question_text', 'question_tags']
        widgets = {
            'question_text': forms.Textarea(attrs={'rows': 1, 'cols': 40}),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text']
        widgets = {
            'answer_text': forms.Textarea(attrs={'rows': 1, 'cols': 40}),
        }
