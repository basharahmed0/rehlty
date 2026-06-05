from django.contrib import admin
from .models import User
from .models import DataUser
from .models import payment

# Register your models here.
admin.site.register(payment)


admin.site.register(User)

@admin.register(DataUser)
class DataUserAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phone_number', 'checkin', 'checkout', 'number_of_rooms', 'number_of_individuals')
    search_fields = ('fullname', 'email', 'phone_number')
    list_filter = ('checkin', 'checkout')
