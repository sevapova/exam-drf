from rest_framework import generics, permissions
from apps.appointments.models import Appointment, PatientProfile
from apps.appointments.serializers import AppointmentSerializer
from apps.appointments.permissions import IsAppointmentOwnerOrAdmin
from rest_framework.exceptions import PermissionDenied

class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != "patient":
            raise PermissionDenied("Only patients can book appointments.")
        patient_profile = PatientProfile.objects.get(user=self.request.user)
        serializer.save(patient=patient_profile)

class MyAppointmentsListView(generics.ListAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "doctor":
            return Appointment.objects.filter(doctor__user=user).select_related("patient__user", "timeslot")
        elif user.role == "patient":
            patient = PatientProfile.objects.get(user=user)
            return Appointment.objects.filter(patient=patient).select_related("doctor__user", "timeslot")
        elif user.role == "admin":
            return Appointment.objects.all()
        return Appointment.objects.none()

class AppointmentDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAppointmentOwnerOrAdmin]
    queryset = Appointment.objects.all()
