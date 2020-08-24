# Generated by Django 3.1 on 2020-08-24 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosComentarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfil', models.CharField(max_length=500)),
                ('comentario', models.CharField(max_length=500)),
                ('cantidad_palabras', models.PositiveIntegerField()),
                ('comentarios_repetidos', models.DecimalField(decimal_places=2, max_digits=3)),
                ('insultos', models.DecimalField(decimal_places=2, max_digits=3)),
                ('emoticones', models.DecimalField(decimal_places=2, max_digits=3)),
                ('multimedia', models.DecimalField(decimal_places=2, max_digits=3)),
                ('links', models.DecimalField(decimal_places=2, max_digits=3)),
                ('comentarios_raros', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]
