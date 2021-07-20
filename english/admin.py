from django.contrib import admin

from . models import EnglishWord

class EnglishAdmin(admin.ModelAdmin):
    list_display = ('uz', 'en',)

admin.site.register(EnglishWord, EnglishAdmin)
