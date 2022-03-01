import datetime
from django.views.generic.list import ListView
from login_signup.models.appointment import Appointment
from login_signup.models.doctor import Doctor
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class AppointmentsView(ListView):
    """
    Display the appointments for the current user
    """
    model = Appointment
    template_name = 'home/appointments/appointments.html'
    isFilter = False

    def post(self, request, *args, **kwargs):
        """
        If the user wants to display the past prescriptions
        """
        self.isFilter = request.POST.get('displayPast')
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Add the appointment's button to the context
        """

        context = super().get_context_data(**kwargs)

        if self.request.user.has_perm('login_signup.can_use_medical_stuff'):
            context['create_appointment'] = f"""
            <div class="flex flex--row--center-all mb-10">
				<a href="{reverse_lazy('home:add_appointment')}" class="btn btn--light-green">Ajouter un rendez-vous</a>
			</div>
            """

        context['isFilter'] = self.isFilter
        return context

    def get_queryset(self):
        """
        We want to display the appointments for the current user
        """
        queryset = super().get_queryset()
        if self.request.user.has_perm('login_signup.can_use_medical_stuff'):
            doctor = Doctor.objects.get(user=self.request.user)
            userAppointments = queryset.filter(doctor=doctor)
        else:
            userAppointments = queryset.filter(user=self.request.user)

        if not self.isFilter:
            userAppointments = userAppointments.filter(is_active=True)
            # Set is_active to false if the date of the appointment is in the past

            for appointment in userAppointments:
                if appointment.date < datetime.date.today():
                    appointment.is_active = False
                    appointment.save()
                else:
                    appointment.is_active = True
                    appointment.save()

        return userAppointments
