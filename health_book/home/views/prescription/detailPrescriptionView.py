from django.views.generic.detail import DetailView
from login_signup.models.prescription import Prescription


class DetailPrescriptionView(DetailView):
    template_name = 'home/detail_prescription.html'
    model = Prescription
    context_object_name = 'prescription'
