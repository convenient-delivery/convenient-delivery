from django.contrib import admin
from order_processor.models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

#Inline Declarations 
"""class DriverInline(admin.StackedInline):
	model = Driver
	max_num = 1
	can_delete = False

class ProfileInline(admin.StackedInline):
  model = Profile
  extra = 0

class SaleItemInline(admin.TabularInline):
  model = SaleItem
  extra = 0

class CategoryInline(admin.TabularInline):
  model = ItemCategory
  extra = 0 


#Model Admin Classes
class EstablishmentAdmin(admin.ModelAdmin):
  inlines = [CategoryInline]
  
class CategoryAdmin(admin.ModelAdmin):
  inlines = [SaleItemInline]
  list_display = ('name','establishment') 
  list_filter = ('establishment',)
  search_fields = ['name']
class UserAdmin(AuthUserAdmin):
	inlines = [DriverInline,ProfileInline]
#class CityAdmin(admin.ModelAdmin):

# unregister old user admin
admin.site.unregister(User)
# register new user admin
admin.site.register(User, UserAdmin)
"""

# Register your models here.
admin.site.register(City)
admin.site.register(Profile)
admin.site.register(Establishment)
admin.site.register(ItemCategory)
admin.site.register(SaleItem)
admin.site.register(Driver)
admin.site.register(Order)
admin.site.register(Address)

