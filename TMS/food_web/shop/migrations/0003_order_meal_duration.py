# Generated by Django 3.1 on 2021-01-17 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='meal_duration',
            field=models.CharField(default='', max_length=111),
        ),
    ]
