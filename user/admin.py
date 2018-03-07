from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Group

admin.site.register(Group)
admin.site.register(User)
