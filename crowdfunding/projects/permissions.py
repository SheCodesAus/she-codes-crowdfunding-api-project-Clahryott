from rest_framework import permissions

#custom permissions for project owner only to be able to edit
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #is the logged in user the owner?
            return True
        return obj.owner == request.user #if it's true - the they should be able to edit 