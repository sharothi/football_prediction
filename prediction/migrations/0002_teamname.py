# Generated by Django 5.0.1 on 2024-01-21 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]