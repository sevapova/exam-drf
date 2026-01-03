from django.db import models
from apps.users.models import User
from apps.doctors.models import DoctorProfile, TimeSlot

class PatientProfile(models.Model):
    GENDER_CHOICES = (("male", "Male"), ("female", "Female"))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return f"{self.user.username}"

class Appointment(models.Model):
    STATUS_CHOICES = (("pending", "Pending"), ("confirmed", "Confirmed"), ("cancelled", "Cancelled"))

    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name="appointments")
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name="appointments")
    timeslot = models.OneToOneField(TimeSlot, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.user.username} → {self.doctor.user.username} ({self.status})"
