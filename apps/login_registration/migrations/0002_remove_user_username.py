# Generated by Django 2.0.6 on 2018-06-17 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]