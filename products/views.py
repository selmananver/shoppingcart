from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def index(request):
    featured_product = Product.objects.order_by('priority')[:4]
    latest_product = Product.objects.order_by('-id')[:4]
    return render(request,'index.html',{'featured_product':featured_product,'latest_product':latest_product})

def list_products(request):
     page = 1
     if request.GET :
          page = request.GET.get('page',1)
     
     product_list = Product.objects.order_by('priority')
     product_paginator = Paginator(product_list,2)
     product_list= product_paginator.get_page(page)
     return render(request,'products_layout.html',{'product_list':product_list})
def detail_products(request,id):
     product = Product.objects.get(id=id)
     return render(request,'product_detail.html',{'product':product})
