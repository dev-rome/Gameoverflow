# Generated by Django 4.0.5 on 2022-07-03 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameoverflow', '0002_answer_user_question_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
