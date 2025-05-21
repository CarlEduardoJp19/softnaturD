from django.urls import path
from . import views
from django.conf import settings
urlpatterns = [
    path('', views.producto, name='producto'),
    path('login/', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('register/', views.register_view , name='register'),
    path('logout/', views.logout_view, name='logout'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
