# from django.views import View
from django.views.generic.edit import FormView
from django.shortcuts import render
from home import forms


class AddAppointment(FormView):
    """Add an appointment to the user"""

    template_name = 'home/add_appointment.html'
    form = forms.AddAppointmentForm
    success_url = 'home:appointments'

    # def get(self, request):
    #     """Display the form to add an appointment"""
    #     # form = forms.AddAppointmentForm()
    #     context = {
    #         'form': self.form
    #     }
    #     return render(request, self.template_name, context)

    # def post(self, request):
    #     """Add the appointment to the database"""
    #     form = self.form(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return render(request, self.template_name, {'form': form})
