
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include ('todo.urls')),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('', include ('productos.urls', namespace='productos')),
]
