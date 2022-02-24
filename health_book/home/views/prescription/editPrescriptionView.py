from django.views.generic.edit import UpdateView
from login_signup.models.prescription import Prescription
from home.forms import AddPrescriptionForm


class EditPrescriptionView(UpdateView):

    model = Prescription
    template_name = 'home/prescription/edit_prescription.html'
    success_url = '/home/prescription/'
    form_class = AddPrescriptionForm
