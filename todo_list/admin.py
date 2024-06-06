from django.contrib import admin
from django.db.models import Count
from .models import Category, Task

admin.site.register(Category)
admin.site.register(Task)