from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Category, Brand, Supplier
from .forms import ProductForm, CategoryForm, BrandForm, SupplierForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Products - Productos
def product_list(request):
    products_list = Product.objects.all()
    
    # Paginación: 10 productos por página
    paginator = Paginator(products_list, 10)
    page = request.GET.get('page')
    
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un entero, mostrar la primera página
        products = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera de rango, mostrar la última página
        products = paginator.page(paginator.num_pages)
    
    # Contexto con las variables necesarias para la paginación
    context = {
        'products': products,
        'paginator': paginator,
        'page_obj': products,
        'is_paginated': paginator.num_pages > 1
    }
    
    return render(request, 'product_list.html', context)

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def product_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('producto:product_list')
        else:
            messages.error(request, f'Error al crear el producto. {form.errors}')
    form = ProductForm()
    categories = Category.objects.all() 
    suppliers = Supplier.objects.all()
    return render(request, 'product_create.html', {'form': form, 'categories': categories, 'suppliers': suppliers})

def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('producto:product_list')
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_uppdate.html', {'form': form, 'product': product})

def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    messages.success(request, 'Producto eliminado exitosamente.')
    return redirect('producto:product_list')

# Categories - Categorías|
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request, 'category_detail.html', {'category': category})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente.')
            return redirect('producto:category_list')
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form})

def category_update(request, pk):
    category = Category.objects.get(pk=pk)  
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada exitosamente.')
            return redirect('producto:category_list')
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form})

def category_delete(request, pk):
    category = Category.objects.get(pk=pk)
    category.delete()
    messages.success(request, 'Categoría eliminada exitosamente.')
    return redirect('producto:category_list')

# Brands - Marcas   
def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'brand_list.html', {'brands': brands})

def brand_detail(request, pk):
    brand = Brand.objects.get(pk=pk)
    return render(request, 'brand_detail.html', {'brand': brand})

def brand_create(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marca creada exitosamente.')
            return redirect('producto:brand_list')   
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = BrandForm()
    return render(request, 'brand_form.html', {'form': form})

def brand_update(request, pk):
    brand = Brand.objects.get(pk=pk)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, 'Marca actualizada exitosamente.')
            return redirect('producto:brand_list')
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = BrandForm(instance=brand)
    return render(request, 'brand_form.html', {'form': form})

def brand_delete(request, pk):
    brand = Brand.objects.get(pk=pk)
    brand.delete()
    messages.success(request, 'Marca eliminada exitosamente.')
    return redirect('producto:brand_list')

# Suppliers - Proveedores
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_list.html', {'suppliers': suppliers})

def supplier_detail(request, pk):
    supplier = Supplier.objects.get(pk=pk)
    return render(request, 'supplier_detail.html', {'supplier': supplier})

def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor creado exitosamente.')
            return redirect('producto:supplier_list')
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = SupplierForm()
    return render(request, 'supplier_form.html', {'form': form})

def supplier_update(request, pk):
    supplier = Supplier.objects.get(pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor actualizado exitosamente.')
            return redirect('producto:supplier_list')
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'supplier_form.html', {'form': form})

def supplier_delete(request, pk):
    supplier = Supplier.objects.get(pk=pk)
    supplier.delete()
    messages.success(request, 'Proveedor eliminado exitosamente.')
    return redirect('producto:supplier_list')