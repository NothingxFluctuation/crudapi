from django.contrib import admin
from .models import DModel
# Register your models here.



class DModel_Admin(admin.ModelAdmin):
    list_display = ('name','driver','host','port','username','password')

admin.site.register(DModel, DModel_Admin)