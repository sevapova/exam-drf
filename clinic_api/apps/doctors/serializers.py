from rest_framework import serializers
from apps.doctors.models import DoctorProfile, TimeSlot
from django.utils import timezone

class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = "__all__"

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = "__all__"

    def validate(self, attrs):
        doctor = self.context['request'].user.doctorprofile
        date = attrs.get("date")
        start_time = attrs.get("start_time")
        end_time = attrs.get("end_time")

        overlap = TimeSlot.objects.filter(
            doctor=doctor,
            date=date,
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        if overlap.exists():
            raise serializers.ValidationError("TimeSlot overlaps with existing slot.")

        if date < timezone.now().date():
            raise serializers.ValidationError("Cannot create slot in the past.")
        return attrs
