from django.db import models
from django.contrib.auth.models import User

# Create your models here.

<<<<<<< HEAD
class City(models.Model):
=======
class Store(models.Model):
>>>>>>> e275d7d2b3c79b61a4b81fef6bdf1ccdc822e1a1

	city = models.CharField(max_length=255) 
	description = models.CharField(max_length=255) 
	currently_open = models.BooleanField(default=False)

	def __unicode__(self):  # Python 3: def __str__(self):
		return self.city	

class Profile(models.Model):

<<<<<<< HEAD
=======

>>>>>>> e275d7d2b3c79b61a4b81fef6bdf1ccdc822e1a1
  user =	models.OneToOneField(User)
  housenumber = models.CharField(max_length=255)
  street = models.CharField(max_length=255)
  apt_sweet = models.CharField(max_length=255,blank=True)
  city = 	models.CharField(max_length=255)
  state = models.CharField(max_length=255)
  zipcode = models.CharField(max_length=255)
	
  phone = models.CharField(max_length=255)

	

  def __unicode__(self):  # Python 3: def __str__(self):
    return self.user.username


class Establishment(models.Model):

  name = models.CharField(max_length=255)
  address = models.TextField(max_length=255)
  phone = models.CharField(max_length=255)

  def __unicode__(self):
    return self.name

class ItemCategory(models.Model):

  establishment = models.ForeignKey(Establishment)
  name = models.CharField(max_length=255)

  def __unicode__(self):  # Python 3: def __str__(self):
    return self.name

class SaleItem(models.Model):
 
  category = models.ForeignKey(ItemCategory)
  name = models.CharField(max_length=255)  
  description = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=50, decimal_places=2)

  def __unicode__(self):
    return self.name

class Driver(models.Model):
	# add drivers hours, active or not
 
  user = models.OneToOneField(User)
<<<<<<< HEAD
  city = models.ForeignKey(City)
=======
  store = models.ForeignKey(Store)	
>>>>>>> e275d7d2b3c79b61a4b81fef6bdf1ccdc822e1a1
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

  user = models.ForeignKey(User)
  order = models.TextField()
  status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='q')
  
<<<<<<< HEAD
  city = models.ForeignKey(City)
=======
  store = models.ForeignKey(Store)
>>>>>>> e275d7d2b3c79b61a4b81fef6bdf1ccdc822e1a1
  driver = models.ForeignKey(Driver)
  date = models.DateTimeField()
  delivered = models.BooleanField(default=False)
  work_required = models.BooleanField(default=False) #This would be true if an order needed to be placed

  cost = models.DecimalField(max_digits=50, decimal_places=2)

  def __unicode__(self):  # Python 3: def __str__(self):
    return self.username
