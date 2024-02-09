from django.shortcuts import render,redirect
from .models import Order,OrderedItem
from products.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def cart(request):
        user = request.user
        customer = user.customer_profile
        cart_obj,created =Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        context ={'cart':cart_obj}

        return render(request,'cart.html',context)

def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        quantity =int(request.POST.get('quantity'))
        productid=request.POST.get('productid')
        cart_obj,created =Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product =Product.objects.get(pk=productid)
        ordered_item,created=OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj
        )
        if created:
             ordered_item.quantity= quantity
             ordered_item.save()
        else:
             ordered_item.quantity =ordered_item.quantity+quantity
             ordered_item.save()
        return redirect('cart')
    
def remove_item_from_cart(request,pk):
     ordered_item =OrderedItem.objects.get(pk=pk)
     if ordered_item:
          ordered_item.delete()
     return redirect('cart')

def checkout_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profile
        total =float(request.POST.get('total'))
        order_object=Order.objects.get(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        if order_object:
            order_object.order_status=Order.ORDER_CONFIRMED
            order_object.total_price=total
            order_object.save()
            status_message ='Your Order is processed. Your item will be delivered within 2 days'
            messages.success(request,status_message)
        else:
             status_message ='Unable to process order. No items in cart'
             messages.error(request,status_message)
    return redirect('cart')


@login_required(login_url='account')

def orders(request):
      user = request.user
      customer = user.customer_profile
      all_orders = Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
      context ={'all_orders':all_orders}
      return render(request,'orders.html',context)
     

    

