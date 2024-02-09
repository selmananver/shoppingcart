from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Customer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def showaccount(request):
    context={}
    if request.POST and 'register' in request.POST:
                context['register'] = True
                try:
                    username =request.POST.get('username')
                    email =request.POST.get('email')
                    password= request.POST.get('password')
                    address= request.POST.get('address')
                    phone= request.POST.get('phone')
                    user = User.objects.create_user(
                    username=username,
                    email =email,
                    password=password
                    )
                    customer = Customer.objects.create(
                        name=username,
                        user=user,
                        address= address,
                        phone=phone
                    )
                    success_message ='User registered successfully'
                    messages.success(request,success_message)
                except Exception as e:
                 error_message ='Duplicate username or invalid input'
                 messages.error(request,error_message)
                
    if request.POST and 'login' in request.POST:
                   context['register'] = False
                   username = request.POST.get('username')
                   password =request.POST.get('password')
                   user = authenticate(username=username,password=password)
                   if user :
                    login(request,user)
                    return redirect('home')
                   else:
                    messages.error(request,'Invalid inputs')
    return render(request,'account.html',context)

def signout(request):
     logout(request)
     return redirect('home')