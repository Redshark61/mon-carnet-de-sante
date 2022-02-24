from django.shortcuts import render
from login_signup.models.appointment import Appointment
from login_signup.models.prescription import Prescription
from login_signup.models.doctor import Doctor
from django.views import View


# @login_required(login_url='index')
class HomeView(View):
    """
    Home page view
    """
    template_name = 'home/home.html'

    def get(self, request):
        if request.user.has_perm('login_signup.can_use_medical_stuff'):
            me = Doctor.objects.get(user=request.user)
            appointment = Appointment.objects.filter(doctor=me, is_active=True)
        else:
            appointment = Appointment.objects.filter(user=request.user, is_active=True)
        context = {
            'user': request.user,
            'appointments': appointment,
        }
        context['prescriptions'] = Prescription.objects.filter(user=self.request.user)

        return render(request, self.template_name, context)
