from django.contrib import admin
from gameoverflow.models import Question, Answer

myImports = [Question, Answer]

# Register your models here.
admin.site.register(myImports)