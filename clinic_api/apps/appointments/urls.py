from django.urls import path
from apps.appointments.views import AppointmentCreateView, MyAppointmentsListView, AppointmentDetailUpdateDeleteView

urlpatterns = [
    path("", AppointmentCreateView.as_view(), name="appointment-create"),
    path("me/", MyAppointmentsListView.as_view(), name="my-appointments"),
    path("<int:pk>/", AppointmentDetailUpdateDeleteView.as_view(), name="appointment-detail"),
]
