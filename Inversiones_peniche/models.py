from django.db import models
import datetime
from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
# Create your models here.


class Telefono(models.Model):
    numero_telefono = models.IntegerField
    numero_cel = models.IntegerField


class Persona(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    apellido = models.CharField(max_length=100, blank=True)
    fecha_nacimiento = models.DateTimeField(default=timezone.now())
    cedula = models.CharField(max_length=20, blank=True)
    correo = models.CharField(max_length=35, blank=True)
    direccion = models.CharField(max_length=50, blank=True)
    Telefonos = models.ForeignKey(Telefono, on_delete=models.CASCADE, default="123")


class Tipo(models.Model):
    tipo = models.CharField(max_length=50)


class Vehiculo(models.Model):
    matricula = models.CharField(unique=True, max_length=40)
    modelo = models.CharField
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    color = models.CharField
    condicion = models.CharField
    valor_mercado = models.IntegerField


class Rol(models.Model):
    nombre = models.CharField


class Operador(Persona):
    fecha_contratacion = models.DateField


class Cuota(models.Model):
    mora_acumulada = models.FloatField
    vencida = models.BooleanField


class Prestamo(models.Model):
    cuotas = models.ForeignKey(Cuota, on_delete=models.CASCADE)
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)
    operador = models.OneToOneField(Operador, on_delete=models.CASCADE)
    fecha_actual = models.DateTimeField
    fecha_primer_pago = models.DateTimeField
    monto_prestado = models.FloatField
    frecuencia_pago = models.CharField(max_length=30)
    taza_interes = models.FloatField
    monto_capital = models.FloatField
    monto_interes = models.FloatField
    tipo_prestamo = models.CharField
    estado = models.CharField
    monto_total = models.FloatField
    total_cuotas_pagadas = models.IntegerField
    fecha_ultimo_pago = models.DateTimeField
    monto_ultimo_pago = models.DateTimeField
    intereses_vencidoes = models.FloatField


class Cliente(Persona):
        vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
        prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)

        def get_absolute_url(self):
            return reverse('base_site', kwargs={'pk': self.pk})


class Factura (models.Model):
    tipo = models.CharField
    cliente = models.OneToOneField(Cliente)
    prestamo = models.OneToOneField(Prestamo)
    cuota = models.OneToOneField(Cuota)
    usuario = models.OneToOneField(Operador)
    nombre_usuario = models.CharField
    fecha = models.DateTimeField
    monto_total = models.FloatField
    balance_deudor = models.FloatField
    monto_capital = models.FloatField
    monto_interes = models.FloatField


class Usuario(Persona):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    password_salt = models.CharField(max_length=30)
    last_log = models.DateTimeField
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)




