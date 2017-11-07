# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171029_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='ativo',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='carga_horaria',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='id',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='professor',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='tipo',
        ),
        migrations.AddField(
            model_name='curso',
            name='idcurso',
            field=models.AutoField(db_column='IdCurso', default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='sigla',
            field=models.CharField(db_column='Sigla', default=1, max_length=5, verbose_name='Sigla'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='curso',
            name='nome',
            field=models.CharField(db_column='Nome', max_length=50, verbose_name='Nome do Curso'),
        ),
    ]