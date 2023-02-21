from rest_framework.permissions import BasePermission


class ModeratorPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method.upper() in ['DELETE', 'POST']:
            return request.user.has_perms([
                'materails.create_course',
                'materails.delete_course',
            ])
        return True
