from django.contrib import admin

from .models import AppConfiguration, Account


admin.site.register(AppConfiguration)
admin.site.register(Account)
