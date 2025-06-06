# Generated by Django 5.2.1 on 2025-05-29 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('clave', models.CharField(max_length=90)),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('numTelefono', models.CharField(max_length=10)),
                ('rol', models.CharField(choices=[('admin', 'Administrador'), ('cliente', 'Cliente')], default='cliente', max_length=20)),
            ],
        ),
    ]
