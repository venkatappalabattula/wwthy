# Generated by Django 4.1.2 on 2022-10-13 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forminput',
            name='name',
        ),
    ]
