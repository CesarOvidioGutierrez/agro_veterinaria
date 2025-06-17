from django import template
from django.utils.safestring import mark_safe
from producto.models import Product
from django.db.models import Q
import random

register = template.Library()

@register.filter
def get_item(lst, index):
    """
    Obtiene un elemento de una lista por su índice
    Uso: {{ mi_lista|get_item:0 }}
    """
    try:
        return lst[index]
    except (IndexError, TypeError):
        return ""

@register.inclusion_tag('components/ofertas_especiales.html')
def mostrar_ofertas(cantidad=3):
    """
    Muestra ofertas especiales (productos seleccionados aleatoriamente)
    Uso: {% mostrar_ofertas %}
    Uso con cantidad específica: {% mostrar_ofertas 5 %}
    """
    # En un escenario real, esto podría ser productos con descuento
    # Aquí simplemente seleccionamos algunos productos al azar
    productos = Product.objects.filter(stock__gt=0).order_by('?')[:cantidad]
    
    return {
        'productos': productos,
        'descuentos': [random.randint(5, 30) for _ in range(len(productos))]
    }

@register.simple_tag
def calcular_precio_oferta(precio, descuento):
    """
    Calcula el precio con descuento para una oferta
    Uso: {% calcular_precio_oferta producto.precio 15 %}
    """
    try:
        precio = float(precio)
        descuento = float(descuento)
        precio_final = precio - (precio * descuento / 100)
        return round(precio_final, 2)
    except:
        return precio

@register.filter
def badge_oferta(descuento):
    """
    Muestra una etiqueta visual para el descuento
    Uso: {{ descuento|badge_oferta }}
    """
    try:
        descuento = int(descuento)
        if descuento >= 20:
            return mark_safe(f'<span class="px-2 py-1 text-xs font-bold text-white bg-red-600 rounded-full">¡{descuento}% OFF!</span>')
        elif descuento >= 10:
            return mark_safe(f'<span class="px-2 py-1 text-xs font-bold text-white bg-orange-500 rounded-full">¡{descuento}% OFF!</span>')
        else:
            return mark_safe(f'<span class="px-2 py-1 text-xs font-bold text-white bg-green-600 rounded-full">¡{descuento}% OFF!</span>')
    except:
        return "" 