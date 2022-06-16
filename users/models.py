from enum import unique
from pyexpat import model
from tabnanny import verbose
from django.db import models
import uuid

"""
Model desenvolvida por Bruno Cristiano
"""

class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class User(models.Model):
    unique_id = MyUUIDModel()
    firstName = models.CharField(max_length=255, blank=False, verbose_name='Primeiro Nome')
    lastName = models.CharField(max_length=255, blank=False, verbose_name='Ultimo Nome')
    cpf = models.CharField(max_length=14, blank=False, verbose_name='CPF')
    email = models.EmailField(max_length=255, blank=False, verbose_name='E-mail')


    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = "Usuários"

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
