from django import forms
from .models import Product, Category, Brand, Supplier

COMMON_INPUT_CLASSES = (
    'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg '
    'focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 '
    'dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 '
    'dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category', 'supplier', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': COMMON_INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': COMMON_INPUT_CLASSES}),
            'price': forms.NumberInput(attrs={'class': COMMON_INPUT_CLASSES}),
            'stock': forms.NumberInput(attrs={'class': COMMON_INPUT_CLASSES}),
            'category': forms.Select(attrs={'class': COMMON_INPUT_CLASSES}),
            'supplier': forms.Select(attrs={'class': COMMON_INPUT_CLASSES}),
            'image': forms.FileInput(attrs={'class': COMMON_INPUT_CLASSES}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': COMMON_INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': COMMON_INPUT_CLASSES}),
        }

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': COMMON_INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': COMMON_INPUT_CLASSES}),
        }

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'description', 'address', 'phone', 'email', 'website']
        widgets = {
            'name': forms.TextInput(attrs={'class': COMMON_INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': COMMON_INPUT_CLASSES}),
            'address': forms.Textarea(attrs={'class': COMMON_INPUT_CLASSES}),
            'phone': forms.TextInput(attrs={'class': COMMON_INPUT_CLASSES}),
            'email': forms.EmailInput(attrs={'class': COMMON_INPUT_CLASSES}),
            'website': forms.URLInput(attrs={'class': COMMON_INPUT_CLASSES}),
        }

