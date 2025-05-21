from django.contrib.auth import logout,authenticate
from django.shortcuts import render, redirect
from .forms import registerForm, loginForm
from django.contrib.auth.hashers import make_password, check_password
from .models import usuario

# Create your views here.

def login(request):
    return render(request, "todo/login.html")

def dashboard(request):
    return render(request,"todo/dashboard.html")

def index(request):
    return render(request,"todo/index.html")

def nosotros(request):
    return render(request,"todo/nosotros.html")

def producto(request):
    return render(request,"todo/producto.html")

def contacto(request):
    return render(request,"todo/contacto.html")

def register(request):
    return render(request, "todo/register.html")

def producto(request):
    usuario_id = request.session.get('usuario_id')  # Obtiene el usuario de la sesión
    return render(request, "todo/producto.html", {"usuario_id": usuario_id})

def register_view(request):
    mensaje = ""
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            clave = form.cleaned_data['clave'] #form.cleaned_data se usa preguntar a la db sobre esas tablas
            email = form.cleaned_data['email']
            numTelefono = form.cleaned_data['numTelefono']

            if usuario.objects.filter(nombre=nombre).exists():
                mensaje = "Este usuario ya existe"
            else:
                clave_hash = make_password(clave) #Se encripta la contraseña
                nuevo_usuario = usuario(nombre=nombre, clave=clave_hash, email=email, numTelefono=numTelefono)
                nuevo_usuario.save()
                return redirect('login')
    else:
        form = registerForm()
    
    return render(request, "todo/register.html", {"form": form, "mensaje": mensaje})

def login_view(request):
    mensaje = ""
    if request.method == "POST":
        form = loginForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            clave = form.cleaned_data['clave']

            try:
                user = usuario.objects.get(nombre = nombre)
                if check_password(clave, user.clave):
                    request.session['usuario_id'] = user.id  # Guarda el ID en la sesión
                    request.session['nombre'] = user.nombre  # Guarda el nombre en la sesión
                    print("Usuario autenticado:", request.session.get('usuario_id'))  # Depuración
                    return redirect('producto')
                else:
                    mensaje = "contraseña incorrecta"
            except usuario.DoesNotExist:
                mensaje = "Nombre de usuario no registrado"
    else:
        form = loginForm()
    return render(request, 'todo/login.html', {'form': form, 'mensaje': mensaje})

def producto(request):
    # Obtiene el ID del usuario guardado en la sesión (si existe)
    usuario_id = request.session.get('usuario_id')  # Obtiene la sesión

    # Retorna la plantilla 'producto.html' y le pasa la variable 'usuario_id'
    # Esto permite saber si el usuario está logueado o no en el HTML
    return render(request, "todo/producto.html", {"usuario_id": usuario_id})

def logout_view(request):
    # Borra todos los datos de la sesión, es decir, "cierra sesión"
    request.session.flush()  # Borra toda la sesión
    # Redirige al usuario a la vista de login después de cerrar sesión
    return redirect('login')
