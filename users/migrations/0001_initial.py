# Generated by Django 4.0.5 on 2022-06-16 02:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUUIDModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255, verbose_name='Primeiro Nome')),
                ('lastName', models.CharField(max_length=255, verbose_name='Ultimo Nome')),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
        ),
    ]
