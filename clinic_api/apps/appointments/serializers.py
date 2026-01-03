from rest_framework import serializers
from apps.appointments.models import Appointment, PatientProfile
from apps.doctors.models import TimeSlot
from django.utils import timezone

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"

    def validate(self, attrs):
        timeslot = attrs.get("timeslot")
        patient = attrs.get("patient")
        doctor = attrs.get("doctor")

        if timeslot.date < timezone.now().date():
            raise serializers.ValidationError("Cannot book appointment in the past.")

        if not timeslot.is_available:
            raise serializers.ValidationError("TimeSlot is not available.")

        if patient.user == doctor.user:
            raise serializers.ValidationError("Doctor cannot book appointment for self.")

        return attrs

    def create(self, validated_data):
        timeslot = validated_data['timeslot']
        timeslot.is_available = False
        timeslot.save()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        status = validated_data.get("status", instance.status)
        if status == "cancelled" and instance.status != "cancelled":
            instance.timeslot.is_available = True
            instance.timeslot.save()
        return super().update(instance, validated_data)
