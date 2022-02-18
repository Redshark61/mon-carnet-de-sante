from django.views.generic.edit import FormView
from django.shortcuts import render
from home import forms
from django.urls import reverse_lazy


class AddAppointment(FormView):
    """
    Add an appointment to the user
    """

    template_name = 'home/add_appointment.html'
    form_class = forms.AddAppointmentForm
    success_url = reverse_lazy('home:appointments')

    def form_valid(self, form):
        """
        If the form is valid, we save it and redirect to the appointments page
        """
        form.save()
        return super().form_valid(form)
