from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Producto(models.Model):

    nombre = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    descripcion = models.TextField()

    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    imagen = models.ImageField(
        upload_to='productos/'
    )

    disponible = models.BooleanField(default=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        self.slug = slugify(self.nombre)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):

    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('procesando', 'Procesando'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
    )

    usuario = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    nombre = models.CharField(max_length=200)

    email = models.EmailField()

    telefono = models.CharField(max_length=20)

    direccion = models.TextField()

    ciudad = models.CharField(max_length=100)

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='pendiente'
    )

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f'Pedido #{self.id}'

class DetallePedido(models.Model):

    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE
    )

    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE
    )

    cantidad = models.IntegerField()

    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):

        return self.producto.nombre