from django.contrib import admin
from . models import User
from django.contrib.admin.decorators import display

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')
    search_fields = ('name', 'email')
    readonly_fields = ('password',)

