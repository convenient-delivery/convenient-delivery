from django import forms
from order_processor import models

class StoreSelect(forms.Form):
  stores = models.Store.objects.all() 
  store_choices = ()

  attrs = {'class' : 'selectpicker show-menu-arrow', 'data-width' : 'auto'}
  widget = forms.Select(attrs=attrs)

  for store in stores:
      store_choices = store_choices + ((store, store),) #Tuple of tuples for the choices

  store = forms.ChoiceField(choices=store_choices, label='', widget=widget)

class login(forms.Form):
  username = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'color': 'black'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'selectpicker show-menu-arrow', 'data-width' : 'auto'}))

class signup(forms.Form):
  username = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'color': 'black'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'selectpicker show-menu-arrow', 'data-width' : 'auto'}))
  driver = forms.BooleanField(required = False, label='driver')
