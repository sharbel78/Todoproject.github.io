# Generated by Django 4.2.6 on 2023-11-18 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task1',
            name='date',
            field=models.DateField(default='1990-03-22'),
            preserve_default=False,
        ),
    ]
