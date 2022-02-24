from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from login_signup.models import appointment
from home.forms import AddAppointmentForm


class EditAppointementView(UpdateView):
    model = appointment.Appointment
    form_class = AddAppointmentForm
    template_name = 'home/appointments/editAppointment.html'

    def get_success_url(self):
        return reverse_lazy('home:appointments')
