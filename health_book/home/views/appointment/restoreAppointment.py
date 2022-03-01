from django.views import View
from django.shortcuts import render
from login_signup.models.appointment import Appointment
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

decorators = [
    permission_required('login_signup.can_use_medical_stuff', raise_exception=True),
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class RestoreAppointementView(View):
    template_name = 'home/appointments/restoreAppointement.html'

    def get(self, request, **kwargs):
        appointment = Appointment.objects.get(id=kwargs['pk'])
        context = {
            'appointment': appointment
        }
        return render(request, self.template_name, context)

    @staticmethod
    def post(request, **kwargs):
        appointment = Appointment.objects.get(id=kwargs['pk'])
        appointment.is_active = True
        appointment.save()
        return render(request, 'home/appointments/restoreAppointementSuccess.html')
