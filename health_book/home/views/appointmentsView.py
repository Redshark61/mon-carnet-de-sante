from django.views.generic.list import ListView
from login_signup.models.appointment import Appointment


class AppointmentsView(ListView):
    model = Appointment
    template_name = 'home/appointments.html'

    def get_queryset(self):
        queryset = super(AppointmentsView, self).get_queryset()
        print(queryset)
        userAppointments = queryset.filter(user=self.request.user)
        print(userAppointments)
        return userAppointments
