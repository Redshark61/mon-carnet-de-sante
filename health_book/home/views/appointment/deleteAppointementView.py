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
class DeleteAppointementView(View):
    template_name = 'home/appointments/deleteAppointement.html'

    def get(self, request, **kwargs):
        appointment = Appointment.objects.get(id=kwargs['pk'])
        print(appointment.is_active)
        context = {
            'appointment': appointment
        }
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        appointment = Appointment.objects.get(id=kwargs['pk'])
        appointment.is_active = False
        appointment.save()
        print(appointment.is_active)
        return render(request, 'home/appointments/deleteAppointementSuccess.html')
