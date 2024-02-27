from django.contrib import admin
from rules.models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


class PathAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


class CapacityAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Path, PathAdmin)
admin.site.register(Capacity, CapacityAdmin)
admin.site.register(Species, SpeciesAdmin)
