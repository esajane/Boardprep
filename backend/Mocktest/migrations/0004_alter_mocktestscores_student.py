# Generated by Django 4.2.4 on 2023-12-08 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
        ('Mocktest', '0003_alter_mocktestscores_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mocktestscores',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_scores', to='User.student'),
        ),
    ]