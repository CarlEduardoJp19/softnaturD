from django.shortcuts import render, redirect
from .models import usuario
from .forms import loginForm, registerForm
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

def login(request):
    return render(request, 'usuarios/login.html')

def register(request):
    return render(request, 'usuarios/register.html')

def nosotros(request):
    return render(request, 'usuarios/nosotros.html')

def contacto(request):
    return render(request,"usuarios/contacto.html")

def index(request):
    return render(request,"usuarios/index.html")


def register_view(request):
    mensaje = ""
    if request.method == "POST":
        form = registerForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            clave = form.cleaned_data['clave'] #form.cleaned_data se usa preguntar a la db sobre esas tablas
            email = form.cleaned_data['email']
            numTelefono = form.cleaned_data['numTelefono']

            if usuario.objects.filter(email=email).exists():
                mensaje = "Este email ya ha sido registrado"
            else:
                clave_hash = make_password(clave) #Se encripta la contraseña
                nuevo_usuario = usuario(nombre=nombre, clave=clave_hash, email=email, numTelefono=numTelefono)
                nuevo_usuario.save()
                return redirect('usuarios:login')
    else:
        form = registerForm()
    
    return render(request, "usuarios/register.html", {"form": form, "mensaje": mensaje})

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
                
                    if user.rol == 'admin':
                        return redirect('dashboard')
                    else:
                        return redirect('productos:producto')
                else:   
                    mensaje = "contraseña incorrecta"
            except usuario.DoesNotExist:
                mensaje = "Nombre de usuario no registrado"
    else:
        form = loginForm()
    return render(request, 'usuarios/login.html', {'form': form, 'mensaje': mensaje})


def logout_view(request):
    # Borra todos los datos de la sesión, es decir, "cierra sesión"
    request.session.flush()  # Borra toda la sesión
    # Redirige al usuario a la vista de login después de cerrar sesión
    return redirect('usuarios:login')
