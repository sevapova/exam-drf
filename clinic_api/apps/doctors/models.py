from django.db import models
from apps.users.models import User

class DoctorProfile(models.Model):
    GENDER_CHOICES = (("male", "Male"), ("female", "Female"))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return f"Dr. {self.user.username} ({self.specialization})"

class TimeSlot(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name="timeslots")
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = ("doctor", "date", "start_time", "end_time")

    def __str__(self):
        return f"{self.date} {self.start_time}-{self.end_time} ({self.doctor.user.username})"
