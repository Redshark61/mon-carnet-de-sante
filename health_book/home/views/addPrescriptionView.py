from django.views.generic import FormView
from home import forms


class AddPrescriptionView(FormView):
    """
    View for the prescription
    """
    template_name = 'home/add_prescription.html'
    form_class = forms.AddPrescriptionForm
    success_url = 'home:prescription'
