# Generated by Django 4.2.7 on 2023-12-10 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0002_page_syllabus'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='page',
            unique_together={('lesson', 'page_number')},
        ),
    ]