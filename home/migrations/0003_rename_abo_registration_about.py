# Generated by Django 4.1.1 on 2022-09-08 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_about_registration_abo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='abo',
            new_name='about',
        ),
    ]
