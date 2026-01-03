from rest_framework import permissions

class IsDoctorOwner(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.doctor.user == request.user
