from django.shortcuts import render

# Create your views here.
def home(request):
    # Breadcrumbs para la página de inicio
    breadcrumbs_items = [
        {'title': 'Inicio', 'url': None}
    ]
    
    return render(request, 'veterinaria/home.html', {
        'title': 'Inicio - Agro Veterinaria',
        'breadcrumbs_items': breadcrumbs_items
    })

def contacto(request):
    # Breadcrumbs para la página de contacto
    breadcrumbs_items = [
        {'title': 'Inicio', 'url': '/'},
        {'title': 'Contacto', 'url': None}
    ]
    
    if request.method == 'POST':
        # En un caso real procesaríamos el formulario aquí
        # Y usaríamos messages para confirmar
        from django.contrib import messages
        messages.success(request, "Tu mensaje ha sido enviado correctamente. Nos pondremos en contacto contigo pronto.")
    
    return render(request, 'veterinaria/contacto.html', {
        'title': 'Contacto - Agro Veterinaria',
        'breadcrumbs_items': breadcrumbs_items
    })
