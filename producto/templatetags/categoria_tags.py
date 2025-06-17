from django import template
from producto.models import Category, Product
from django.db.models import Count

register = template.Library()

@register.inclusion_tag('components/lista_categorias.html')
def mostrar_categorias():
    """
    Muestra una lista de categorías con la cantidad de productos en cada una
    Uso: {% mostrar_categorias %}
    """
    categorias = Category.objects.annotate(
        num_productos=Count('product')
    ).order_by('name')
    
    return {'categorias': categorias}

@register.inclusion_tag('components/menu_categorias.html')
def menu_categorias(categoria_actual=None, current_category=None):
    """
    Genera un menú de navegación para las categorías
    Uso: {% menu_categorias categoria_actual %}
    O: {% menu_categorias categoria_actual current_category=current_category %}
    """
    categorias = Category.objects.all().order_by('name')
    return {
        'categorias': categorias,
        'categoria_actual': categoria_actual,
        'current_category': current_category
    }

@register.simple_tag
def productos_por_categoria(categoria_id):
    """
    Devuelve el número de productos en una categoría
    Uso: {% productos_por_categoria categoria.id %}
    """
    return Product.objects.filter(category_id=categoria_id).count() 