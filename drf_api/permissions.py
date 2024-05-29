from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
  """
    Custom permission to allow read 
    access to all and write access only to the object owner.
    """
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    return obj.owner == request.user