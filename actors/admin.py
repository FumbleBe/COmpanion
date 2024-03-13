from django.contrib import admin
from actors.models import *


class CharacterAdmin(admin.ModelAdmin):

    list_display = ('name', 'size')



admin.site.register(Character, CharacterAdmin)
