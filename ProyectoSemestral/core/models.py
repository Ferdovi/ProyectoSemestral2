from django.db import models 
from django.core.validators import MinValueValidator
    
class Producto(models.Model):
    codigo_producto = models.CharField(max_length=200)
    nombre_producto = models.CharField(max_length=200)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    precio_unitario = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.nombre_producto

class Orden(models.Model):
    numero_orden = models.CharField(max_length=10)
    fecha_orden = models.CharField(max_length=10)
    productos = models.ManyToManyField(Producto)  # Cambiado a ManyToManyField
    rut_cliente = models.CharField(max_length=12)
    nombre_razon_social = models.CharField(max_length=100)
    direccion_cliente = models.CharField(max_length=200)
    telefono_cliente = models.CharField(max_length=15)
    correo_clinte = models.EmailField()
    rut = models.CharField(max_length=12, blank=True, null=True)
    razon_social = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    sitio_web = models.URLField(blank=True, null=True)
    tipo_servicio = models.CharField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return self.numero_orden

class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=200,blank=False,null=False )
    contrasenaUsuario = models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
        return self.nombreUsuario
