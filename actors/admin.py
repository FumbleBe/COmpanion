from django.contrib import admin
from actors.models import *


class ActorAdmin(admin.ModelAdmin):

    list_display = ('name', 'size')



admin.site.register(Actor, ActorAdmin)
