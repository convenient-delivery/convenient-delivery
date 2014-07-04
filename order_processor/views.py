from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from order_processor.models import Store, Establishment
from order_processor import forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User, Group

def index(request):
  #output = "test output"
  
  store_selector = forms.StoreSelect()
  login = forms.login()
  
  context = {
              'store_select' : store_selector,
             'login' : login,
            }
  return render(request, 'order_processor/index.html', context)


def order(request):
  context = {}
  if request.method == 'POST':
    store_selector = forms.StoreSelect(request.POST)

  else:
    return redirect('index')  
  
  

  return render(request, 'order_processor/order.html', context)

@csrf_exempt  
def driver(request):
  context = {}
  username = request.POST['username'] 
  password = request.POST['password']
  user = authenticate(username=username, password=password)
  if user is not None:
    if user.is_active:
      login(request, user)
      return redirect('driver')
    else:
      return redirect('index')
  else:
    return redirect('index')

@csrf_exempt  
def signup(request):
  signup = forms.signup()

  context = {
              'signup' : signup ,
            }
  return render (request, 'order_processor/signup.html', context)

@csrf_exempt  
def successfulsignup(request):
  username = request.POST['username']
  password = request.POST['password']
  driver = request.POST.get('driver', False) 
  user = User.objects.create_user(username, "example@example.com", password)
  if request.method == 'Post'
    
    g = Group.objects.get(name='driver')
    g.user_set.add(user)
    user.save()
    HttpResponse("got here")
    
  user_list = User.objects.all()
  context = {
              'user_list': user_list
            }
  return render(request, 'order_processor/successfulsignup.html', context)
  
