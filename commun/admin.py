from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Client, Benevole, Agenda

admin.site.register(Client)
admin.site.register(Benevole)
admin.site.register(Agenda)