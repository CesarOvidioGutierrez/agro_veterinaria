from django import template
from django.utils.safestring import mark_safe
from django.utils.timezone import now
import datetime

register = template.Library()

@register.simple_tag
def fecha_actual(formato="%d/%m/%Y"):
    """
    Muestra la fecha actual en el formato especificado
    Uso: {% fecha_actual %}
    Uso con formato: {% fecha_actual "%Y-%m-%d" %}
    """
    return now().strftime(formato)

@register.filter
def tiempo_transcurrido(fecha):
    """
    Muestra el tiempo transcurrido desde una fecha en formato humano
    Uso: {{ producto.created_at|tiempo_transcurrido }}
    """
    if not fecha:
        return ""
    
    delta = now() - fecha
    dias = delta.days
    
    if dias == 0:
        segundos = delta.seconds
        if segundos < 60:
            return "hace unos segundos"
        elif segundos < 3600:
            minutos = segundos // 60
            return f"hace {minutos} minuto{'s' if minutos != 1 else ''}"
        else:
            horas = segundos // 3600
            return f"hace {horas} hora{'s' if horas != 1 else ''}"
    elif dias == 1:
        return "ayer"
    elif dias < 7:
        return f"hace {dias} día{'s' if dias != 1 else ''}"
    elif dias < 30:
        semanas = dias // 7
        return f"hace {semanas} semana{'s' if semanas != 1 else ''}"
    elif dias < 365:
        meses = dias // 30
        return f"hace {meses} mes{'es' if meses != 1 else ''}"
    else:
        años = dias // 365
        return f"hace {años} año{'s' if años != 1 else ''}"

@register.inclusion_tag('components/breadcrumbs.html')
def breadcrumbs(items=None):
    """
    Genera un breadcrumb (migas de pan) para la navegación
    Uso: {% breadcrumbs breadcrumb_items %}
    Donde breadcrumb_items es una lista de diccionarios con 'title' y 'url'
    Ejemplo:
    [
        {'title': 'Inicio', 'url': '/'},
        {'title': 'Productos', 'url': '/productos/'},
        {'title': 'Categoría', 'url': None}  # El último sin URL
    ]
    """
    # Si no se proporcionan elementos, usar una ruta predeterminada
    if not items:
        items = [{'title': 'Inicio', 'url': '/'}]
    
    return {'items': items} 