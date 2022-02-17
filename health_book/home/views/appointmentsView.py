from datetime import datetime
from django.views.generic.list import ListView
from login_signup.models.appointment import Appointment
from login_signup.models.doctor import Doctor
from django.urls import reverse_lazy


class AppointmentsView(ListView):
    """
    Display the appointments for the current user
    """
    model = Appointment
    template_name = 'home/appointments.html'

    def get_context_data(self, **kwargs):
        """
        Add the appointment's button to the context
        """

        context = super().get_context_data(**kwargs)

        if self.request.user.has_perm('login_signup.can_use_medical_stuff'):
            print("has the permission")
            context['create_appointment'] = f"""
            <div class="flex flex--row--center-all mb-10">
				<a href="{reverse_lazy('home:add_appointment')}" class="btn btn--light-green">Ajouter un rendez-vous</a>
			</div>
            """
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

        userAppointments = userAppointments.filter(is_active=True)

        # Set is_active to false if the date of the appointment is in the past
        for appointment in userAppointments:
            print(appointment.date)
            print(datetime.date.today())
            if appointment.date < datetime.date.today():
                appointment.is_active = False
                appointment.save()

        userAppointments = userAppointments.filter(is_active=True)

        return userAppointments
