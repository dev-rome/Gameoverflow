# Generated by Django 4.0.5 on 2022-07-06 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameoverflow', '0003_alter_answer_pub_date_alter_question_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer_question',
            new_name='question',
        ),
    ]
