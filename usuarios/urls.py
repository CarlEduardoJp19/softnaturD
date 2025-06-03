from django.urls import path
from . import views
from django.conf import settings

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('contacto/', views.contacto, name="contacto"),
    path('index/', views.index, name="index"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('gstUsuarios/', views.gstUsuarios, name="gstUsuarios"),
    path('loginAdm/', views.loginAdmin, name="loginAdmin"),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
