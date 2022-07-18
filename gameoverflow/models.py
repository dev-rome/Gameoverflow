from multiprocessing.dummy import Array
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.
# quesion model


class Question(models.Model):
    question_title = models.CharField(max_length=200)
    question_text = models.CharField(max_length=200)
    question_tags = ArrayField(models.CharField(max_length=200), size=5)
    question_vote = models.IntegerField(default=0)
    question_answer = models.IntegerField(default=0)
    question_views = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.question_title


class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    answer_vote = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.answer_text
