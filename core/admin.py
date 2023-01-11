from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Product

# Register your models here.

admin.site.site_header = 'Fast Airways Couriers Admin'
admin.site.site_title = 'Fast Airways Couriers Admin Portal'
admin.site.index_title = 'Welcome to Fast Airways Couriers'


admin.site.register(Product)

admin.site.unregister(Group)
