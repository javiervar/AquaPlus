# Generated by Django 2.1.7 on 2019-03-12 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.DateField(default=None)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=50)),
                ('contrasena', models.CharField(max_length=50)),
                ('tipo', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=None)),
                ('cantidad', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aqua_app.TipoVenta')),
            ],
        ),
    ]