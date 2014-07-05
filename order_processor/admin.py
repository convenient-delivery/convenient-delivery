from django.contrib import admin
from order_processor.models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

#Inline Declarations 
class DriverInline(admin.StackedInline):
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
<<<<<<< HEAD
#class CityAdmin(admin.ModelAdmin):
=======
#class StoreAdmin(admin.ModelAdmin):
>>>>>>> e275d7d2b3c79b61a4b81fef6bdf1ccdc822e1a1
	

# unregister old user admin
admin.site.unregister(User)
# register new user admin
admin.site.register(User, UserAdmin)


# Register your models here.
<<<<<<< HEAD
admin.site.register(City)
=======
admin.site.register(Store)
>>>>>>> e275d7d2b3c79b61a4b81fef6bdf1ccdc822e1a1
admin.site.register(Profile)
admin.site.register(Establishment, EstablishmentAdmin)
admin.site.register(ItemCategory, CategoryAdmin)
admin.site.register(SaleItem)
admin.site.register(Driver)
admin.site.register(Order)


