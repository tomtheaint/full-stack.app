from django.contrib import admin

# Register your models here.

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Task._meta.fields]

admin.site.register(Task, TaskAdmin)