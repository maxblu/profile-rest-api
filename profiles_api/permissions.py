# kimitar la posibilidad de los demeas usarios a toketear datos de otro que no sean ellos

from rest_framework import permissions


class UpdateOwnProfile(permissions .BasePermission):
    """
    Alloy to user updating his own profile

    """

    def has_object_permission(self, request, view, obj):
        """
        Check user is trying to edit his own profile
        """

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdatingOwnStatus(permissions.BasePermission):
    """
    Allow user to update they own status
    """

    def has_object_permission(self, request, view, obj):
        """ Check user is trying to update they own status"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
