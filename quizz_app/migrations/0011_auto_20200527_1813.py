# Generated by Django 3.0.6 on 2020-05-27 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizz_app', '0010_results'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='owner',
        ),
        migrations.AddField(
            model_name='results',
            name='player',
            field=models.CharField(max_length=100, null=True),
        ),
    ]