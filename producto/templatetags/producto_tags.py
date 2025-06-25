from django import template
from django.utils.safestring import mark_safe
import locale

register = template.Library()

@register.filter
def formato_precio(value):
    """
    Formatea un precio con símbolo de peso argentino y separadores de miles
    Uso: {{ producto.precio|formato_precio }}
    """
    try:
        # Configurar locale para Argentina
        locale.setlocale(locale.LC_ALL, 'es_AR.UTF-8')
        return f"$ {locale.format_string('%,.2f', float(value), True)}"
    except:
        # Si hay algún error, mostrar formato simple
        return f"$ {value}"

@register.filter
def estado_stock(value):
    """
    Muestra un estado visual del stock:
    - Verde si hay más de 10 unidades
    - Amarillo si hay entre 1 y 10
    - Rojo si no hay stock
    Uso: {{ producto.stock|estado_stock }}
    """
    try:
        stock = int(value)
        if stock <= 0:
            return mark_safe('<span class="px-2 py-1 text-xs font-medium text-white bg-red-500 dark:bg-red-600 rounded-full">Sin stock</span>')
        elif stock <= 10:
            return mark_safe(f'<span class="px-2 py-1 text-xs font-medium text-yellow-800 bg-yellow-200 dark:text-yellow-200 dark:bg-yellow-800 rounded-full">Bajo ({stock})</span>')
        else:
            return mark_safe(f'<span class="px-2 py-1 text-xs font-medium text-green-800 bg-green-200 dark:text-green-200 dark:bg-green-800 rounded-full">Disponible ({stock})</span>')
    except:
        return value

@register.simple_tag
def descuento(precio, porcentaje):
    """
    Calcula el precio con descuento
    Uso: {% descuento producto.precio 10 %}
    """
    try:
        precio = float(precio)
        porcentaje = float(porcentaje)
        precio_con_descuento = precio - (precio * porcentaje / 100)
        return f"$ {precio_con_descuento:.2f}"
    except:
        return "Error en cálculo" 