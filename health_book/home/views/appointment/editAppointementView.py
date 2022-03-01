from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from login_signup.models import appointment
from home.forms import AddAppointmentForm
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

decorators = [
    permission_required('login_signup.can_use_medical_stuff', raise_exception=True),
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class EditAppointementView(UpdateView):
    model = appointment.Appointment
    form_class = AddAppointmentForm
    template_name = 'home/appointments/editAppointment.html'

    def get_success_url(self):
        return reverse_lazy('home:appointments')
