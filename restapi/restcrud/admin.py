from django.contrib import admin
from django.contrib.auth.models import User, Group
# Register your models here.
from .models import Update as UpdateModel
admin.site.unregister(Group)

admin.site.register(UpdateModel)