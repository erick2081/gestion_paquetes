from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),

    # Rutas para Paquetes
    path('paquetes/', views.listar_paquete, name='listar_paquete'),
    path('paquetes/crear/', views.crear_paquete, name='crear_paquete'),
    path('paquetes/editar/<int:paquete_id>/', views.editar_paquete, name='editar_paquete'),
    path('paquetes/eliminar/<int:paquete_id>/', views.eliminar_paquete, name='eliminar_paquete'),

    # Rutas para Reservas
    path('reservas/', views.listar_reserva, name='listar_reserva'),
    path('reservas/crear/', views.crear_reserva, name='crear_reserva'),
    path('reservas/editar/<int:reserva_id>/', views.editar_reserva, name='editar_reserva'),
    path('reservas/eliminar/<int:reserva_id>/', views.eliminar_reserva, name='eliminar_reserva'),


    path('pagos/', views.listar_pago, name='listar_pago'),
    path('pagos/crear/', views.crear_pago, name='crear_pago'),
    path('pagos/editar/<int:pago_id>/', views.editar_pago, name='editar_pago'),
    path('pagos/eliminar/<int:pago_id>/', views.eliminar_pago, name='eliminar_pago'),



    path('comentarios/', views.listar_comentario, name='listar_comentario'),
    path('comentarios/crear/', views.crear_comentario, name='crear_comentario'),
    path('comentarios/editar/<int:comentario_id>/', views.editar_comentario, name='editar_comentario'),
    path('comentarios/eliminar/<int:comentario_id>/', views.eliminar_comentario, name='eliminar_comentario'),



    path('facturas/', views.listar_factura, name='listar_factura'),
    path('facturas/crear/', views.crear_factura, name='crear_factura'),
    path('facturas/editar/<int:factura_id>/', views.editar_factura, name='editar_factura'),
    path('facturas/eliminar/<int:factura_id>/', views.eliminar_factura, name='eliminar_factura'),

    path('indicadores/', views.kpis_view, name='ver_kpis'),
]
