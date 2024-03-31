from django.contrib import admin
from actors.models import *


class CharacterAdmin(admin.ModelAdmin):

    list_display = ('name', 'level', 'gender', 'species', 'profile')


class STRAdmin(admin.ModelAdmin):
    list_display = ("base", "value", "mod")


class DEXAdmin(admin.ModelAdmin):
    list_display = ("base", "value", "mod")


class CONAdmin(admin.ModelAdmin):
    list_display = ("base", "value", "mod")


class INTAdmin(admin.ModelAdmin):
    list_display = ("base", "value", "mod")


class WISAdmin(admin.ModelAdmin):
    list_display = ("base", "value", "mod")


class CHAAdmin(admin.ModelAdmin):
    list_display = ("base", "value", "mod")


admin.site.register(Character, CharacterAdmin)
# admin.site.register(STR, STRAdmin)
# admin.site.register(DEX, DEXAdmin)
# admin.site.register(CON, CONAdmin)
# admin.site.register(INT, INTAdmin)
# admin.site.register(WIS, WISAdmin)
# admin.site.register(CHA, CHAAdmin)
