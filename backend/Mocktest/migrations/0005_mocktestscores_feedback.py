# Generated by Django 4.2.4 on 2023-12-11 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mocktest', '0004_alter_mocktestscores_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='mocktestscores',
            name='feedback',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]