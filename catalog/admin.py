from django.contrib import admin

from catalog.models import Architect, Contractor, Consumer, Plan

admin.site.register(Architect)
admin.site.register(Contractor)
admin.site.register(Consumer)
admin.site.register(Plan)

