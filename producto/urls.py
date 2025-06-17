from django.urls import path
from .views import (
    product_create, product_update, product_delete, product_detail,
    category_list, category_create, category_update, category_delete, category_detail,
    brand_list, brand_create, brand_update, brand_delete, brand_detail,
    supplier_list, supplier_create, supplier_update, supplier_delete, supplier_detail,
    ProductListView
)

app_name = 'producto'

urlpatterns = [
    # Productos
    path('', ProductListView.as_view(), name='product_list'),
    path('nuevo/', product_create, name='product_create'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('<int:pk>/editar/', product_update, name='product_update'),
    path('<int:pk>/eliminar/', product_delete, name='product_delete'),
    
    # Categorías
    path('categorias/', category_list, name='category_list'),
    path('categorias/nuevo/', category_create, name='category_create'),
    path('categorias/<int:pk>/editar/', category_update, name='category_update'),
    path('categorias/<int:pk>/eliminar/', category_delete, name='category_delete'),
    path('categorias/<int:pk>/', category_detail, name='category_detail'),
    
    # Marcas
    path('marcas/', brand_list, name='brand_list'),
    path('marcas/nuevo/', brand_create, name='brand_create'),
    path('marcas/<int:pk>/editar/', brand_update, name='brand_update'),
    path('marcas/<int:pk>/eliminar/', brand_delete, name='brand_delete'),
    path('marcas/<int:pk>/', brand_detail, name='brand_detail'),
    
    # Proveedores
    path('proveedores/', supplier_list, name='supplier_list'),
    path('proveedores/nuevo/', supplier_create, name='supplier_create'),
    path('proveedores/<int:pk>/editar/', supplier_update, name='supplier_update'),
    path('proveedores/<int:pk>/eliminar/', supplier_delete, name='supplier_delete'),
    path('proveedores/<int:pk>/', supplier_detail, name='supplier_detail'),
]
