from rest_framework import permissions


class OwnerAndDmOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if "DungeonMaster" in request.user.groups.all():
            return True

        return obj.owner == request.user


class IsDmOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.groups.filter(name="DungeonMaster").exists()
