from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('products_list',views.list_products,name='list_products'),
    path('product_detail/<id>',views.detail_products,name='product_detail')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)