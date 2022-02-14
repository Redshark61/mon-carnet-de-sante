from django.views.generic.list import ListView
from login_signup.models.appointment import Appointment


class AppointmentsView(ListView):
    """
    Display the appointments for the current user
    """
    model = Appointment
    template_name = 'home/appointments.html'

    def get_queryset(self):
        """
        We want to display the appointments for the current user
        """
        queryset = super().get_queryset()
        userAppointments = queryset.filter(user=self.request.user)
        return userAppointments
