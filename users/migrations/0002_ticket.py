# Generated by Django 3.0.8 on 2020-09-27 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Movie_name', models.CharField(default='', max_length=250)),
                ('date', models.CharField(default='', max_length=250)),
                ('time', models.CharField(default='', max_length=250)),
                ('hall_type', models.CharField(default='', max_length=250)),
                ('total_seat', models.CharField(default='', max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
