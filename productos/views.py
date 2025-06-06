from django.shortcuts import render,redirect
from .forms import registerProduc
from .models import Producto

# Create your views here.

def productos(request):
    products = Producto.objects.all()
    return render(request, 'productos/producto.html', {'products': products})

def list_produc(request):
    return render(request, 'productos/list_produc.html')


def registerProducts(request):
    if request.method == 'POST':
        form = registerProduc(request.POST, request.FILES)
        if form.is_valid():
            Producto.objects.create(
                nombProduc = form.cleaned_data['nombProduc'],
                descripcion= form.cleaned_data['descripcion'],
                Categoria = form.cleaned_data['Categoria'],
                precio = form.cleaned_data['precio'],
                imgProduc = form.cleaned_data['imgProduc'],
            )
            return redirect('productos:listProduc')
    else:
        form = registerProduc()
    return render(request, 'productos/list_produc.html', {'form': form})


def producto(request):
    # Obtiene el ID del usuario guardado en la sesión (si existe)
    usuario_id = request.session.get('usuario_id')  # Obtiene la sesión

    # Retorna la plantilla 'producto.html' y le pasa la variable 'usuario_id'
    # Esto permite saber si el usuario está logueado o no en el HTML
    return render(request, "todo/producto.html", {"usuario_id": usuario_id})


def productos_view(request):
    products = Producto.objects.all()
    usuario_id = request.session.get('usuario_id')  # <-- Obtenemos el ID

    return render(request, 'productos/producto.html', {
        'products': products,
        'usuario_id': usuario_id  # <-- Lo enviamos al template
    })


