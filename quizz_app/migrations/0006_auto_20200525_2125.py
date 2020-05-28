# Generated by Django 3.0.6 on 2020-05-25 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizz_app', '0005_quizzes_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizzes',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to=settings.AUTH_USER_MODEL),
        ),
    ]
