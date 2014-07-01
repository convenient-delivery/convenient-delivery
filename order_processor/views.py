from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from order_processor.models import Store, Establishment
from order_processor import forms

def index(request):
  #output = "test output"
  
  store_selector = forms.StoreSelect()
  
  context = {'store_select' : store_selector}
  return render(request, 'order_processor/index.html', context)


def order(request):
  context = {}
  if request.method == 'POST':
    store_selector = forms.StoreSelect(request.POST)

  else:
    return redirect('index')  
  
  

  return render(request, 'order_processor/order.html', context)
