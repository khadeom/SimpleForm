# Generated by Django 4.0.8 on 2022-11-20 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PersonalContacts',
            new_name='incidentData',
        ),
    ]