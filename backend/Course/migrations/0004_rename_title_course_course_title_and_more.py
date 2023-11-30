# Generated by Django 4.2.7 on 2023-11-26 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0003_syllabus_lesson'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='title',
            new_name='course_title',
        ),
        migrations.RenameField(
            model_name='lesson',
            old_name='title',
            new_name='lesson_title',
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='Course.course'),
        ),
    ]