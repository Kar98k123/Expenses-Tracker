# Generated by Django 4.1.2 on 2023-03-23 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myexpenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexpenses',
            name='Category',
            field=models.CharField(choices=[('Health', 'Health'), ('Electronics', 'Electronics'), (' Travel', ' Travel'), ('Education', 'Education'), ('Books', 'Books'), ('Others', 'Others')], max_length=200),
        ),
    ]
