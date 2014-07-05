from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from order_processor.models import Store, Establishment
from order_processor import forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import AuthenticationForm

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

def login(request):
  if request.user.is_authenticated():
    first_name = request.user.first_name
    last_name = request.user.last_name
    context = {
                'first_name' : first_name,
                'last_name' : last_name,
              }
    return render(request, 'order_processor/alreadyloggedin.html', context)
  else:
    authenticationForm = AuthenticationForm()
  
    context = {
              'authenticationForm': authenticationForm,
             }
    return render (request, 'order_processor/login.html', context)
 
def logout(request):
  auth_logout(request)
  context = {}
  return render(request, 'order_processor/logout.html', context)
 
def signup(request):
  signup = forms.signup()

  context = {
              'signup' : signup ,
            }
  return render (request, 'order_processor/signup.html', context)

def successfulsignup(request):
  username = request.POST['username']
  password = request.POST['password']
  email = request.POST['email']
  first_name = request.POST['first_name']
  last_name = request.POST['last_name']
  user = User.objects.create_user(username, email, password)
  user_list = User.objects.all() 
  user.last_name = last_name
  user.first_name = first_name
  context = {
              'username':username,
              'email':email,
              'first_name':first_name,
              'last_name':last_name,
            }
  return render(request, 'order_processor/successfulsignup.html', context)

def successfullogin(request):
  username = request.POST['username']
  password = request.POST['password']
  username = request.POST['username'] 
  password = request.POST['password']
  user = authenticate(username=username, password=password)
  
  if user is not None: 
    if user.is_active:
      auth_login(request, user)
      first_name = request.user.first_name 
      last_name = request.user.last_name
      context = {
              'first_name' : first_name,
              'last_name' : last_name,
            }
      return render(request, 'order_processor/successfullogin.html', context)
      logged_in = True
    else:
      redirect('index')
  else: 
    redirect('index')

def alreadyloggedin(request):
  if request.user.is_authenticated():
    first_name = request.user.first_name
    last_name = request.user.last_name
    return render(request, 'order_processor/alreadyloggedin.html', context)
  else:
    context = {}
    return render(request, 'order_processor/index.html', context)
