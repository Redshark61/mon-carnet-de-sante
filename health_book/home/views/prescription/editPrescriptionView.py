from django.views.generic.edit import UpdateView
from login_signup.models.prescription import Prescription
from home.forms import AddPrescriptionForm
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

decorators = [
    permission_required('login_signup.can_use_medical_stuff', raise_exception=True),
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class EditPrescriptionView(UpdateView):

    model = Prescription
    template_name = 'home/prescription/edit_prescription.html'
    success_url = '/home/prescription/'
    form_class = AddPrescriptionForm
