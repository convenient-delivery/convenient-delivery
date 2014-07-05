from django import forms
from order_processor import models

<<<<<<< HEAD
class CitySelect(forms.Form):
  cities = models.City.objects.all() 
  city_choices = ()
=======
class StoreSelect(forms.Form):
  cities = models.Store.objects.all() 
  store_choices = ()
>>>>>>> e275d7d2b3c79b61a4b81fef6bdf1ccdc822e1a1

  attrs = {'class' : 'selectpicker show-menu-arrow', 'data-width' : 'auto'}
  widget = forms.Select(attrs=attrs)

<<<<<<< HEAD
  for city in cities:
      city_choices = city_choices + ((city, city),) #Tuple of tuples for the choices

  city = forms.ChoiceField(choices=city_choices, label='', widget=widget)
=======
  for store in cities:
      store_choices = store_choices + ((store, store),) #Tuple of tuples for the choices

  store = forms.ChoiceField(choices=store_choices, label='', widget=widget)
>>>>>>> e275d7d2b3c79b61a4b81fef6bdf1ccdc822e1a1

class login(forms.Form):
  username = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'color': 'black'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'selectpicker show-menu-arrow', 'data-width' : 'auto'}))

class signup(forms.Form):
  username = forms.CharField(max_length = 100, widget = forms.TextInput(attrs={'color': 'black'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={
                                                                'class' : 'selectpicker show-menu-arrow', 
                                                                'data-width' : 'auto'
                                                              }))
  email = forms.EmailField(max_length=254)
  first_name = forms.CharField(max_length = 100, widget = forms.TextInput({}))
  last_name = forms.CharField(max_length = 100, widget = forms.TextInput({}))
  
  def clean_username(self):
    username = self.cleaned_data['username']
    if User.objects.exclude(pk = self.instance.pk).filter(username=username).exists():
      raise forms.ValidationError(u'Username "%s" is already in use.' % username)
    return username 
