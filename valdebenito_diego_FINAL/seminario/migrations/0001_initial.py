# Generated by Django 4.2.4 on 2023-12-19 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Inscrito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=15)),
                ('fecha_inscripcion', models.DateField(auto_now_add=True)),
                ('hora_inscripcion', models.TimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('RESERVADO', 'Reservado'), ('COMPLETADA', 'Completada'), ('ANULADA', 'Anulada'), ('NO ASISTEN', 'No Asisten')], max_length=20)),
                ('observacion', models.TextField()),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminario.institucion')),
            ],
        ),
    ]
