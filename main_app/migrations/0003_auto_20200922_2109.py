# Generated by Django 3.0.8 on 2020-09-22 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20200921_1927'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['timeChoices']},
        ),
    ]
