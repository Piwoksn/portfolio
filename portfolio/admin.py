from django.contrib import admin
from .models import Message, Project

class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']

# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Project)