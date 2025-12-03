from django.contrib import admin
from .models import Courses, Classes

# Register your models here.
admin.site.register(Classes)
admin.site.register(Courses)
admin.site.register(Comments)