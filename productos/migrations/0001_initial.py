# Generated by Django 2.0.5 on 2018-08-10 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('Precio1', models.FloatField(blank=True, null=True)),
                ('Rango1', models.FloatField(blank=True, null=True)),
                ('Precio2', models.FloatField(blank=True, null=True)),
                ('Rango2', models.FloatField(blank=True, null=True)),
                ('Precio3', models.FloatField(blank=True, null=True)),
                ('Rango3', models.FloatField(blank=True, null=True)),
                ('Precio4', models.FloatField(blank=True, null=True)),
                ('Rango4', models.FloatField(blank=True, null=True)),
                ('Precio5', models.FloatField(blank=True, null=True)),
                ('Rango5', models.FloatField(blank=True, null=True)),
                ('Precio6', models.FloatField(blank=True, null=True)),
                ('Rango6', models.FloatField(blank=True, null=True)),
                ('Precio7', models.FloatField(blank=True, null=True)),
                ('Rango7', models.FloatField(blank=True, null=True)),
                ('Precio8', models.FloatField(blank=True, null=True)),
                ('Rango8', models.FloatField(blank=True, null=True)),
                ('Precio9', models.FloatField(blank=True, null=True)),
                ('Rango9', models.FloatField(blank=True, null=True)),
                ('Precio10', models.FloatField(blank=True, null=True)),
                ('Rango10', models.FloatField(blank=True, null=True)),
                ('Precio11', models.FloatField(blank=True, null=True)),
                ('Rango11', models.FloatField(blank=True, null=True)),
                ('Precio12', models.FloatField(blank=True, null=True)),
                ('Rango12', models.FloatField(blank=True, null=True)),
                ('medida', models.CharField(max_length=50)),
                ('IdMaterial', models.CharField(max_length=30)),
            ],
        ),
    ]
