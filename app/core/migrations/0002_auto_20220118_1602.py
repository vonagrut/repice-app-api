# Generated by Django 2.1.15 on 2022-01-18 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_staf',
            new_name='is_staff',
        ),
    ]
