
from django.urls import path
from . import views

app_name = 'producto'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('nuevo/', views.product_create, name='product_create'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/editar/', views.product_update, name='product_update'),
    path('<int:pk>/eliminar/', views.product_delete, name='product_delete'),
    path('categorias/', views.category_list, name='category_list'),
    path('categorias/nuevo/', views.category_create, name='category_create'),
    path('categorias/<int:pk>/editar/', views.category_update, name='category_update'),
    path('categorias/<int:pk>/eliminar/', views.category_delete, name='category_delete'),
    path('categorias/<int:pk>/', views.category_detail, name='category_detail'),
    path('marcas/', views.brand_list, name='brand_list'),
    path('marcas/nuevo/', views.brand_create, name='brand_create'),
    path('marcas/<int:pk>/editar/', views.brand_update, name='brand_update'),
    path('marcas/<int:pk>/eliminar/', views.brand_delete, name='brand_delete'),
    path('marcas/<int:pk>/', views.brand_detail, name='brand_detail'),
    path('proveedores/', views.supplier_list, name='supplier_list'),
    path('proveedores/nuevo/', views.supplier_create, name='supplier_create'),
    path('proveedores/<int:pk>/editar/', views.supplier_update, name='supplier_update'),
    path('proveedores/<int:pk>/eliminar/', views.supplier_delete, name='supplier_delete'),
    path('proveedores/<int:pk>/', views.supplier_detail, name='supplier_detail'),
]
