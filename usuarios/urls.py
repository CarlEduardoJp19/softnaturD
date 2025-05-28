from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('contacto/', views.contacto, name="contacto"),
    path('index/', views.index, name="index"),
    path('nosotros/', views.nosotros, name="nosotros"),
]
