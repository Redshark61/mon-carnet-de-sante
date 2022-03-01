from django.views.generic.detail import DetailView
from login_signup.models.prescription import Prescription
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class DetailPrescriptionView(DetailView):
    template_name = 'home/prescription/detail_prescription.html'
    model = Prescription
    context_object_name = 'prescription'
