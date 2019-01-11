from django.contrib import admin

from catalog.models import Author, CompanyUser, PrivateUser, Plan

admin.site.register(Author)
admin.site.register(CompanyUser)
admin.site.register(PrivateUser)
admin.site.register(Plan)
