from django.contrib import admin
from .models import Contact  # Don't forget to import your model

# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'message', 'created_at')

admin.site.register(Contact)
