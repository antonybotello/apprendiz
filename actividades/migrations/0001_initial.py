# Generated by Django 4.1.7 on 2023-04-27 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Llamado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45, verbose_name='Nombre')),
                ('norma', models.CharField(max_length=45, verbose_name='Norma')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Llamado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField(auto_now=True, help_text='MM/DD/AAAA', verbose_name='Fecha')),
                ('descripcion', models.CharField(max_length=45, verbose_name='Descripción')),
                ('estado', models.CharField(choices=[('1', 'Activo'), ('0', 'Inactivo')], default='1', max_length=1, verbose_name='Estado')),
                ('tipo_llamado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividades.tipo_llamado', verbose_name='Tipo de Llamado')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name='Usuario')),
            ],
        ),
    ]
