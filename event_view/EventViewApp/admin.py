from django.contrib import admin

from .models import Event, Info
from django.contrib.auth.admin import UserAdmin

admin.site.register(Event)
admin.site.register(Info)