# Generated by Django 4.0.4 on 2022-04-26 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sapp', '0005_smodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smodel',
            name='user',
        ),
    ]