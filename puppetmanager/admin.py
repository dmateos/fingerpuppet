from django.contrib import admin

from .models import Configuration, Classification, Node


admin.site.register(Configuration)
admin.site.register(Classification)
admin.site.register(Node)
