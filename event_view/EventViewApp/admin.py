from django.contrib import admin

from .models import Event
from django.contrib.auth.admin import UserAdmin

admin.site.register(Event)