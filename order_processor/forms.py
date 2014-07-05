from django import forms
from order_processor import models

class StoreSelect(forms.Form):
  cities = models.Store.objects.all() 
  store_choices = ()

  attrs = {'class' : 'selectpicker show-menu-arrow', 'data-width' : 'auto'}
  widget = forms.Select(attrs=attrs)

  for store in cities:
      store_choices = store_choices + ((store, store),) #Tuple of tuples for the choices

  store = forms.ChoiceField(choices=store_choices, label='', widget=widget)

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
