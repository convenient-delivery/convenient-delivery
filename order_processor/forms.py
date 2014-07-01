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


