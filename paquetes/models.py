from django.db import models

class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = (
        ('cliente', 'Cliente'),
        ('administrador', 'Administrador'),
    )
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)
    contraseña_hash = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Paquete(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion = models.IntegerField()  # duración en días
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cantidad_personas = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"Reserva de {self.usuario.nombre} para {self.paquete.nombre}"

class Pago(models.Model):
    METODO_PAGO_CHOICES = (
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
        ('efectivo', 'Efectivo'),
    )
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    metodo_pago = models.CharField(max_length=50, choices=METODO_PAGO_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pago = models.CharField(max_length=20, choices=(('pendiente', 'Pendiente'), ('completado', 'Completado'), ('fallido', 'Fallido')))
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago de {self.monto} para la reserva {self.reserva.id}"
    


class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)
    comentario = models.TextField()
    calificacion = models.IntegerField(choices=[(1, '1 Estrella'), (2, '2 Estrellas'), (3, '3 Estrellas'), (4, '4 Estrellas'), (5, '5 Estrellas')])
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.usuario.nombre} para {self.paquete.nombre}"
    


class Factura(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('emitida', 'Emitida'), ('pagada', 'Pagada')])

    def __str__(self):
        return f"Factura de {self.reserva.id} - {self.estado}"
