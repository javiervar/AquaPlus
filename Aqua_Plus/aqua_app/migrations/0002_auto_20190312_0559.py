# Generated by Django 2.1.7 on 2019-03-12 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aqua_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipoventa',
            name='tipo',
            field=models.CharField(max_length=50),
        ),
    ]
