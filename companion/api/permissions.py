from django.contrib.auth.models import User, Group
from rest_framework import permissions


class OwnerAndDmOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        try:
            return (
                Group.objects.get(name="DungeonMaster")
                .user_set.filter(id=request.user.id)
                .exists()
            )
        except Group.DoesNotExist:
            return obj.owner == request.user


# class IsDmOrReadOnly(permissions.BasePermission):

#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         return request.user.groups.filter(name="DungeonMaster").exists()


class IsDmOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.groups.filter(name="DungeonMaster").exists()


class IsDmOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.groups.filter(name="DungeonMaster").exists()


def is_in_group(user, group_name):
  try:
    return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
  except Group.DoesNotExist:
    return False

class HasGroupPermission(permissions.BasePermission):
  def has_permission(self, request, view):
    required_groups = view.permission_groups.get(view.action)
    if required_groups == None:
        return False
    elif '_Public' in required_groups:
        return True
    else:
      return any([is_in_group(request.user, group_name) for group_name in required_groups])
