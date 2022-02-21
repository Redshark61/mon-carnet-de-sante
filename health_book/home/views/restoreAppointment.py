from django.views import View
from django.shortcuts import render
from login_signup.models.appointment import Appointment


class RestoreAppointementView(View):
    template_name = 'home/restoreAppointement.html'

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
        return render(request, 'home/restoreAppointementSuccess.html')
