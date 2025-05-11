from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'veterinaria/home.html', {
        'title': 'Inicio - Agro Veterinaria'
    })

def contacto(request):
    if request.method == 'POST':
        # En un caso real procesaríamos el formulario aquí
        # Y usaríamos messages para confirmar
        from django.contrib import messages
        messages.success(request, "Tu mensaje ha sido enviado correctamente. Nos pondremos en contacto contigo pronto.")
    
    return render(request, 'veterinaria/contacto.html', {
        'title': 'Contacto - Agro Veterinaria'
    })
