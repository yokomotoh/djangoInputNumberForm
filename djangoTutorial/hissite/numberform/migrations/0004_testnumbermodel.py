# Generated by Django 4.0 on 2021-12-29 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('numberform', '0003_remove_todolist_tick'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestNumberModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_number', models.IntegerField(default=0)),
            ],
        ),
    ]
