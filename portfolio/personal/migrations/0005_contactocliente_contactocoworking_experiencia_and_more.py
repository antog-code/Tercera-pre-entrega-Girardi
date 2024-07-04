# Generated by Django 5.0.6 on 2024-07-01 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_rename_añofin_estudios_anio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=12)),
                ('mensaje', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ContactoCoworking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=12)),
                ('mensaje', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('anioInicio', models.DateField()),
                ('anioFin', models.DateField()),
                ('Empresa', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreHabilidad', models.CharField(max_length=50)),
                ('nivel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProyecto', models.CharField(max_length=50)),
                ('anioProyecto', models.DateField()),
                ('descripcion', models.TextField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='AcerdaDeMi',
        ),
        migrations.DeleteModel(
            name='Contacto',
        ),
        migrations.DeleteModel(
            name='Cv',
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
    ]
