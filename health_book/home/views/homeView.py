from django.shortcuts import render
from login_signup.models.appointment import Appointment
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.decorators import login_required


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

        return render(request, self.template_name, context)
