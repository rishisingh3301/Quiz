# Generated by Django 4.1.1 on 2022-09-08 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_registration_about_alter_registration_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='id',
        ),
        migrations.AlterField(
            model_name='registration',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.registration')),
            ],
        ),
    ]
