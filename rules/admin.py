from django.contrib import admin
from rules.choices import Source, ItemTrait
from rules.models import Profile, Path, Capacity, Species


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


class PathAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


class CapacityAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")


class SourceAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ItemTraitAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Path, PathAdmin)
admin.site.register(Capacity, CapacityAdmin)
admin.site.register(Species, SpeciesAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(ItemTrait, ItemTraitAdmin)
