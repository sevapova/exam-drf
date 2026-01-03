from rest_framework import permissions

class IsAppointmentOwnerOrAdmin(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.role == "admin":
            return True
        if user.role == "doctor":
            return obj.doctor.user == user
        if user.role == "patient":
            return obj.patient.user == user
        return False
