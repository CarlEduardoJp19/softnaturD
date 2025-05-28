from django.urls import path
from . import views
from django.conf import settings
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
