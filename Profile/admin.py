from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
admin.site.register(user)
admin.site.register(friend)
admin.site.register(Restaurant)
admin.site.register(FuelStation)
admin.site.register(Hotel)