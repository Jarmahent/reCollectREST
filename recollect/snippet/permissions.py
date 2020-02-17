from rest_framework.permissions import BasePermission

class UserIsOwnerSnippet(BasePermission):

    def has_object_permission(self, request, view, snippet):
        return request.user.id == snippet.user.id