from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views



app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/<int:pk>/', views.products_detail, name='products_detail'),
]


# Добавьте этот код для обслуживания медиафайлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)