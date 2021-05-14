# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *


#
# from .models import SomeLocationModel
# from mapbox_location_field.admin import MapAdmin
# from mapbox_location_field.admin import MapAdmin
# from .models import Place


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class CustomerInLine(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'employee'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (CustomerInLine,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Customer)
admin.site.register(School_info)
admin.site.register(Contact)
admin.site.register(Board_allowed)
admin.site.register(gender)
admin.site.register(Facility)
# admin.site.register(SomeLocationModel, MapAdmin)
# admin.site.register(Place, MapAdmin)
