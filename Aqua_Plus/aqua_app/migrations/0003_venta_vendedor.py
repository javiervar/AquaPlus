# Generated by Django 2.1.7 on 2019-03-15 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aqua_app', '0002_auto_20190312_0559'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='vendedor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='aqua_app.Usuario'),
        ),
    ]
