# Generated by Django 4.2.7 on 2023-12-06 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Institution', '0001_initial'),
        ('Subscription', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('1', 'Chemical Engineering'), ('2', 'Mechanical Engineering'), ('3', 'Electrical Engineering'), ('4', 'Civil Engineering')], max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('registration_date', models.DateField(auto_now_add=True)),
                ('last_login', models.DateField(auto_now=True)),
                ('user_type', models.CharField(choices=[('S', 'Student'), ('T', 'Teacher')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='User.user')),
                ('name', models.CharField(max_length=255)),
                ('institution_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='institutionID_teacher', to='Institution.institution')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.specialization')),
            ],
            bases=('User.user',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='User.user')),
                ('institution_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='institutionID_student', to='Institution.institution')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.specialization')),
                ('subscription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Subscription.subscription')),
            ],
            bases=('User.user',),
        ),
    ]
