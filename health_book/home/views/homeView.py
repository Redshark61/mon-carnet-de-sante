from django.shortcuts import render
from login_signup.models.appointment import Appointment
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


@method_decorator(login_required(login_url='index'), name="get")
class HomeView(View):
    """
    Home page view
    """
    template_name = 'home/home.html'

    def get(self, request):
        appointment = Appointment.objects.filter(user=request.user)
        context = {
            'user': request.user,
            'appointments': appointment,
        }

        # context['isMedical'] = self.request.user.has_perm('login_signup.can_use_medical_stuff')

        return render(request, self.template_name, context)
