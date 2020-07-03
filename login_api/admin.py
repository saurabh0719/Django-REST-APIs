from django.contrib import admin
from .models import Student, Menu, Breakfast, Lunch, Dinner

# Register your models here.
admin.site.register(Student)
admin.site.register(Menu)
admin.site.register(Breakfast)
admin.site.register(Lunch)
admin.site.register(Dinner)