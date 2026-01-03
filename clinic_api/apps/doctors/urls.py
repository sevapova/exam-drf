from django.urls import path
from apps.doctors.views import DoctorListView, TimeSlotCreateView, TimeSlotListView

urlpatterns = [
    path("", DoctorListView.as_view(), name="doctor-list"),
    path("timeslots/", TimeSlotListView.as_view(), name="timeslot-list"),
    path("timeslots/create/", TimeSlotCreateView.as_view(), name="timeslot-create"),
]
