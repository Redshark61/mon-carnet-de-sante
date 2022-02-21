from django.views import View
from django.shortcuts import render
from login_signup.models.appointment import Appointment


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
