from rest_framework import generics, filters
from apps.doctors.models import DoctorProfile, TimeSlot
from apps.doctors.serializers import DoctorProfileSerializer, TimeSlotSerializer
from apps.users.permissions import IsDoctor
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

class DoctorListView(generics.ListAPIView):
    serializer_class = DoctorProfileSerializer
    queryset = DoctorProfile.objects.select_related("user").all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["specialization"]
    search_fields = ["user__username", "specialization"]
    ordering_fields = ["experience_years"]

class DoctorTimeSlotListView(generics.ListAPIView):
    serializer_class = TimeSlotSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["date", "is_available"]
    ordering_fields = ["date", "start_time"]

    def get_queryset(self):
        doctor_id = self.kwargs["pk"]
        return TimeSlot.objects.filter(doctor__id=doctor_id, is_available=True)
