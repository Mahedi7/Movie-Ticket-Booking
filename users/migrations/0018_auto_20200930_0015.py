# Generated by Django 3.0.8 on 2020-09-29 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_remove_ticket_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='date',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='hall_type',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='time',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='total_seat',
            field=models.CharField(max_length=250),
        ),
    ]
