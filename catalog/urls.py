from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views







app_name = 'catalog'

urlpatterns = [
    path('', views.ProductList.as_view(), name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='products_detail'),
    path('product/create/', views.ProductCrearte.as_view(), name='product_create'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete')
]


# Добавьте этот код для обслуживания медиафайлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)