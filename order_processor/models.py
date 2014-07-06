from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from decimal import *
# Create your models here.

class City(models.Model):

	city = models.CharField(max_length=255) 
	description = models.CharField(max_length=255) 
	currently_open = models.BooleanField(default=False)

	def __unicode__(self):  # Python 3: def __str__(self):
		return self.city	

class Address(models.Model):
  address_line_1 = models.CharField(max_length=255)
  address_line_2 = models.CharField(max_length=255, blank = True, null = True)
  city = models.CharField(max_length=255)
  state = models.CharField(max_length=255)
  zipcode = models.CharField(max_length=255)

  class Category(models.Model):
    class Meta:
      verbose_name = "Address"

  def __unicode__(self):
    return self.address_line_1

class Profile(models.Model):

  user =	models.OneToOneField(User)
  address = models.ForeignKey(Address, blank = True, null = True)
  phone = models.CharField(max_length=255)

  def __unicode__(self):  # Python 3: def __str__(self):
    return self.user.username

class SaleItem(models.Model):
 
  name = models.CharField(max_length=255)  
  description = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=50, decimal_places=2)
  establishment = models.OneToOneField('Establishment', null = True) #quotes required because model is not defined yet!
  category = models.OneToOneField('ItemCategory', null = True)

  def __unicode__(self):
    return self.name

class ItemCategory(models.Model):

  name = models.CharField(max_length=255)
  establishment = models.OneToOneField('Establishment', null = True) #quotes required because model is not defined yet!

  def __unicode__(self):  # Python 3: def __str__(self):
    return self.name

class Establishment(models.Model):

  name = models.CharField(max_length=255)
  address = models.OneToOneField(Address, null = True)
  phone = models.CharField(max_length=255)
  
  def __unicode__(self):
    return self.name

class Driver(models.Model):
	# add drivers hours, active or not
 
  user = models.OneToOneField(User)
  city = models.ForeignKey(City)
  currently_active = models.BooleanField(default=False)
  phone = models.CharField(max_length=255)

  def __unicode__(self):  # Python 3: def __str__(self):
    return self.user.username

class Order(models.Model):

  STATUS_CHOICES = (
    ('q', 'In Queue'),
    ('p', 'Pick Up'),
    ('r', 'On Route'),
    ('d', 'Delivered'),
  )
  profile = models.ForeignKey(Profile, null = True)
  items = models.ManyToManyField(SaleItem, null = True) 
  status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='q') 
  city = models.ForeignKey(City)
  driver = models.ForeignKey(Driver)
  date = models.DateTimeField()
  delivered = models.BooleanField(default=False)
  work_required = models.BooleanField(default=False) #This would be true if an order needed to be placed
  cost = models.DecimalField(max_digits=50, decimal_places=2, null = True) 

  def __unicode__(self):  # Python 3: def __str__(self):
    self_order = models.ForeignKey('self')
    current_city = self.city
    current_username = self.profile.user.username 
    name = "CITY / " + current_city.city + " | " + "USERNAME / " + current_username + " | "  
    items_list = self.items.all()
    for saleitem in items_list:
      name = name + "ESTABLISHMENT / " + saleitem.establishment.name + " | "
    return name 
    
 
