from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.productos_view, name="producto"),
    path('gstproduct/', views.registerProducts, name="listProduc"),
]
