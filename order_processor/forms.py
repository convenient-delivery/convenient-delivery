from django import forms
from order_processor.models import *

class CitySelect(forms.Form):
  cities = City.objects.all() 

  attrs = {'class' : 'selectpicker show-menu-arrow', 'data-width' : 'auto'}
  widget = forms.Select(attrs=attrs)


  city = forms.ModelChoiceField(queryset = cities, label='', widget=widget, empty_label = None)

class EstablishmentSelect(forms.Form):
  def __init__(self, *args, **kwargs):
    establishment_list = kwargs.pop('establishment_list')
    super(EstablishmentSelect, self).__init__(*args, **kwargs)
    self.fields['establishment'] = forms.ModelChoiceField(queryset = establishment_list, empty_label = None)

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
