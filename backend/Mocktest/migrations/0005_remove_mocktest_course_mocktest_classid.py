# Generated by Django 4.2.4 on 2023-12-08 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Class', '0001_initial'),
        ('Mocktest', '0004_alter_mocktestscores_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mocktest',
            name='course',
        ),
        migrations.AddField(
            model_name='mocktest',
            name='classID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Class.class'),
        ),
    ]