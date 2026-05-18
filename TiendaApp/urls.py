from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),

    path(
        'producto/<slug:slug>/',
        views.detalle_producto,
        name='detalle_producto'
    ),

    path('carrito/', views.carrito, name='carrito'),

path(
    'agregar/<int:producto_id>/',
    views.agregar_producto,
    name='agregar_producto'
),

path(
    'eliminar/<int:producto_id>/',
    views.eliminar_producto,
    name='eliminar_producto'
),

path(
    'restar/<int:producto_id>/',
    views.restar_producto,
    name='restar_producto'
),

path(
    'limpiar/',
    views.limpiar_carrito,
    name='limpiar_carrito'
),

 # urls de regitro 
 
path('registro/', views.registro, name='registro'),

path(
    'login/',
    views.iniciar_sesion,
    name='login'
),

path(
    'logout/',
    views.cerrar_sesion,
    name='logout'
),

path(
    'checkout/',
    views.checkout,
    name='checkout'
),

path(
    'dashboard/',
    views.dashboard,
    name='dashboard'
),
path(
    'mis-pedidos/',
    views.mis_pedidos,
    name='mis_pedidos'
),

path(
    'pedido/<int:pedido_id>/',
    views.detalle_pedido,
    name='detalle_pedido'
),
path('crear-producto/', views.crear_producto, name='crear_producto'),
path(
    'dashboard/producto/eliminar/<int:producto_id>/',
    views.eliminar_producto_admin,
    name='eliminar_producto_admin'
),

path(
    'dashboard/pedido/eliminar/<int:pedido_id>/',
    views.eliminar_pedido_admin,
    name='eliminar_pedido_admin'
),

path(
    'dashboard/usuario/eliminar/<int:usuario_id>/',
    views.eliminar_usuario_admin,
    name='eliminar_usuario_admin'
),
 path('accounts/', include('django.contrib.auth.urls')),
    # o manualmente:
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]