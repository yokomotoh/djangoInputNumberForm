# Generated by Django 4.0 on 2021-12-29 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('numberform', '0002_alter_todolist_options_remove_todolist_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='tick',
        ),
    ]
