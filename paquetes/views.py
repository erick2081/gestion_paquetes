from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario,Paquete,Reserva,Pago,Comentario,Factura

def listar_usuarios(request):
    usuarios = Usuario.objects.all()  # Obtenemos todos los usuarios
    return render(request, 'listar.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        correo = request.POST['correo']
        tipo_usuario = request.POST['tipo_usuario']
        # Aquí agregaríamos la lógica para crear el usuario
        Usuario.objects.create(nombre=nombre, correo_electronico=correo, tipo_usuario=tipo_usuario)
        messages.success(request, 'Usuario creado correctamente.')
        return redirect('listar_usuarios')
    return render(request, 'crear.html')

def editar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    if request.method == 'POST':
        usuario.nombre = request.POST['nombre']
        usuario.correo_electronico = request.POST['correo']
        usuario.tipo_usuario = request.POST['tipo_usuario']
        usuario.save()
        messages.success(request, 'Usuario editado correctamente.')
        return redirect('listar_usuarios')
    return render(request, 'editar.html', {'usuario': usuario})

def eliminar_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    usuario.delete()
    messages.success(request, 'Usuario eliminado correctamente.')
    return redirect('listar_usuarios')





# Listar Paquetes (cambiamos el nombre a listar_paquete)
def listar_paquete(request):
    paquetes = Paquete.objects.all()
    return render(request, 'listapaquete.html', {'paquetes': paquetes})

# Crear Paquete
def crear_paquete(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        duracion = request.POST['duracion']
        Paquete.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            duracion=duracion
        )
        messages.success(request, 'Paquete creado correctamente.')
        return redirect('listar_paquete')
    return render(request, 'crearpaquete.html')

# Editar Paquete
def editar_paquete(request, paquete_id):
    paquete = Paquete.objects.get(id=paquete_id)
    if request.method == 'POST':
        paquete.nombre = request.POST['nombre']
        paquete.descripcion = request.POST['descripcion']
        paquete.precio = request.POST['precio']
        paquete.duracion = request.POST['duracion']
        paquete.save()
        messages.success(request, 'Paquete editado correctamente.')
        return redirect('listar_paquete')
    return render(request, 'editarpaquete.html', {'paquete': paquete})

# Eliminar Paquete
def eliminar_paquete(request, paquete_id):
    paquete = Paquete.objects.get(id=paquete_id)
    paquete.delete()
    messages.success(request, 'Paquete eliminado correctamente.')
    return redirect('listar_paquete')




def listar_reserva(request):
    reservas = Reserva.objects.all()
    return render(request, 'listareserva.html', {'reservas': reservas})

# Crear Reserva
def crear_reserva(request):
    if request.method == 'POST':
        usuario_id = request.POST['usuario']
        paquete_id = request.POST['paquete']
        fecha_inicio = request.POST['fecha_inicio']
        fecha_fin = request.POST['fecha_fin']
        cantidad_personas = request.POST['cantidad_personas']
        total = request.POST['total']
        estado = request.POST['estado']

        usuario = Usuario.objects.get(id=usuario_id)
        paquete = Paquete.objects.get(id=paquete_id)

        Reserva.objects.create(
            usuario=usuario,
            paquete=paquete,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            cantidad_personas=cantidad_personas,
            total=total,
            estado=estado
        )
        messages.success(request, 'Reserva creada correctamente.')
        return redirect('listar_reserva')

    usuarios = Usuario.objects.all()
    paquetes = Paquete.objects.all()
    return render(request, 'creareserva.html', {'usuarios': usuarios, 'paquetes': paquetes})

# Editar Reserva
def editar_reserva(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    if request.method == 'POST':
        reserva.usuario = Usuario.objects.get(id=request.POST['usuario'])
        reserva.paquete = Paquete.objects.get(id=request.POST['paquete'])
        reserva.fecha_inicio = request.POST['fecha_inicio']
        reserva.fecha_fin = request.POST['fecha_fin']
        reserva.cantidad_personas = request.POST['cantidad_personas']
        reserva.total = request.POST['total']
        reserva.estado = request.POST['estado']
        reserva.save()
        messages.success(request, 'Reserva editada correctamente.')
        return redirect('listar_reserva')

    usuarios = Usuario.objects.all()
    paquetes = Paquete.objects.all()
    return render(request, 'editarreserva.html', {'reserva': reserva, 'usuarios': usuarios, 'paquetes': paquetes})

# Eliminar Reserva
def eliminar_reserva(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    reserva.delete()
    messages.success(request, 'Reserva eliminada correctamente.')
    return redirect('listar_reserva')





def listar_pago(request):
    pagos = Pago.objects.all()
    return render(request, 'listarpago.html', {'pagos': pagos})

# Crear Pago
def crear_pago(request):
    if request.method == 'POST':
        reserva_id = request.POST['reserva']
        metodo_pago = request.POST['metodo_pago']
        monto = request.POST['monto']
        estado_pago = request.POST['estado_pago']

        reserva = Reserva.objects.get(id=reserva_id)  # Obtenemos la reserva

        Pago.objects.create(
            reserva=reserva,
            metodo_pago=metodo_pago,
            monto=monto,
            estado_pago=estado_pago
        )
        messages.success(request, 'Pago creado correctamente.')
        return redirect('listar_pago')

    reservas = Reserva.objects.all()
    return render(request, 'crearpago.html', {'reservas': reservas})

# Editar Pago
def editar_pago(request, pago_id):
    pago = Pago.objects.get(id=pago_id)
    if request.method == 'POST':
        pago.metodo_pago = request.POST['metodo_pago']
        pago.monto = request.POST['monto']
        pago.estado_pago = request.POST['estado_pago']
        pago.save()
        messages.success(request, 'Pago editado correctamente.')
        return redirect('listar_pago')

    return render(request, 'editarpago.html', {'pago': pago})

# Eliminar Pago
def eliminar_pago(request, pago_id):
    pago = Pago.objects.get(id=pago_id)
    pago.delete()
    messages.success(request, 'Pago eliminado correctamente.')
    return redirect('listar_pago')




def listar_comentario(request):
    comentarios = Comentario.objects.all()
    return render(request, 'listarcomentario.html', {'comentarios': comentarios})

# Crear Comentario
def crear_comentario(request):
    if request.method == 'POST':
        usuario_id = request.POST['usuario']
        paquete_id = request.POST['paquete']
        comentario = request.POST['comentario']
        calificacion = request.POST['calificacion']

        usuario = Usuario.objects.get(id=usuario_id)
        paquete = Paquete.objects.get(id=paquete_id)

        Comentario.objects.create(
            usuario=usuario,
            paquete=paquete,
            comentario=comentario,
            calificacion=calificacion
        )
        messages.success(request, 'Comentario creado correctamente.')
        return redirect('listar_comentario')

    usuarios = Usuario.objects.all()
    paquetes = Paquete.objects.all()
    return render(request, 'crearcomentario.html', {'usuarios': usuarios, 'paquetes': paquetes})

# Editar Comentario
def editar_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    if request.method == 'POST':
        comentario.comentario = request.POST['comentario']
        comentario.calificacion = request.POST['calificacion']
        comentario.save()
        messages.success(request, 'Comentario editado correctamente.')
        return redirect('listar_comentario')

    return render(request, 'editarcomentario.html', {'comentario': comentario})

# Eliminar Comentario
def eliminar_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    comentario.delete()
    messages.success(request, 'Comentario eliminado correctamente.')
    return redirect('listar_comentario')


########################################


def listar_factura(request):
    facturas = Factura.objects.all()
    return render(request, 'listarfactura.html', {'facturas': facturas})

# Crear Factura
def crear_factura(request):
    if request.method == 'POST':
        reserva_id = request.POST['reserva']
        pago_id = request.POST['pago']
        monto_total = request.POST['monto_total']
        estado = request.POST['estado']

        reserva = Reserva.objects.get(id=reserva_id)
        pago = Pago.objects.get(id=pago_id)

        Factura.objects.create(
            reserva=reserva,
            pago=pago,
            monto_total=monto_total,
            estado=estado
        )
        messages.success(request, 'Factura creada correctamente.')
        return redirect('listar_factura')

    reservas = Reserva.objects.all()
    pagos = Pago.objects.all()
    return render(request, 'crearfactura.html', {'reservas': reservas, 'pagos': pagos})

# Editar Factura
def editar_factura(request, factura_id):
    factura = Factura.objects.get(id=factura_id)
    if request.method == 'POST':
        factura.monto_total = request.POST['monto_total']
        factura.estado = request.POST['estado']
        factura.save()
        messages.success(request, 'Factura editada correctamente.')
        return redirect('listar_factura')

    return render(request, 'editarfactura.html', {'factura': factura})

# Eliminar Factura
def eliminar_factura(request, factura_id):
    factura = Factura.objects.get(id=factura_id)
    factura.delete()
    messages.success(request, 'Factura eliminada correctamente.')
    return redirect('listar_factura')






from django.db.models import Count, Sum, Avg
from django.shortcuts import render
import json

def kpis_view(request):
    total_usuarios = Usuario.objects.count()
    total_paquetes = Paquete.objects.count()
    total_reservas = Reserva.objects.count()

    reservas_activas = Reserva.objects.filter(estado='activo').count()
    reservas_finalizadas = Reserva.objects.filter(estado='finalizado').count()
    reservas_canceladas = Reserva.objects.filter(estado='cancelado').count()

    ingresos_totales = Reserva.objects.aggregate(total=Sum('total'))['total'] or 0

    paquete_mas_reservado = Reserva.objects.values('paquete__nombre') \
        .annotate(total=Count('id')).order_by('-total').first()

    usuario_mas_reservas = Reserva.objects.values('usuario__nombre') \
        .annotate(total=Count('id')).order_by('-total').first()

    indicadores = {
        'Total Usuarios': total_usuarios,
        'Total Paquetes': total_paquetes,
        'Total Reservas': total_reservas,
        'Reservas Activas': reservas_activas,
        'Reservas Finalizadas': reservas_finalizadas,
        'Reservas Canceladas': reservas_canceladas,
        'Ingresos Totales': ingresos_totales,
        'Paquete Más Reservado': paquete_mas_reservado['paquete__nombre'] if paquete_mas_reservado else 'Sin datos',
        'Usuario con Más Reservas': usuario_mas_reservas['usuario__nombre'] if usuario_mas_reservas else 'Sin datos',
    }

    # Datos para los gráficos
    labels_estado = ['Activas', 'Finalizadas', 'Canceladas']
    valores_estado = [reservas_activas, reservas_finalizadas, reservas_canceladas]

    return render(request, 'kpis.html', {
        'indicadores': indicadores,
        'labels_estado': json.dumps(labels_estado),
        'valores_estado': json.dumps(valores_estado),
    })







