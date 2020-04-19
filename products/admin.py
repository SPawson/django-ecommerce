from django.contrib import admin
from .models import Product

# Register your models here.

#Registering the model, can be used in the admin panel
admin.site.register(Product)