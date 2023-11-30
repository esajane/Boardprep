# Generated by Django 4.2.7 on 2023-11-30 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_user_first_name_user_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('S', 'Student'), ('T', 'Teacher')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
