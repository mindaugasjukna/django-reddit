from rest_framework import permissions


class isOwnerOrNoAccess(permissions.BasePermissions):
    def has_object_permission(self, request, view, obj):
        return obj.user = request.user
