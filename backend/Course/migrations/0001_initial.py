# Generated by Django 4.2.7 on 2023-11-20 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('short_description', models.CharField(max_length=500)),
                ('long_description', models.TextField()),
            ],
        ),
    ]