from django.contrib import admin

from .models import Yarn


class YarnAdmin(admin.ModelAdmin):
    ...


admin.site.register(Yarn, YarnAdmin)