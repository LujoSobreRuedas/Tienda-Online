from django.contrib import admin
from .models import Producto, Pedido, DetallePedido
admin.site.register(Pedido)
admin.site.register(DetallePedido)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'precio',
        'disponible'
    )

    prepopulated_fields = {
        'slug': ('nombre',)
    }
