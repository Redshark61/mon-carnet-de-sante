from django.views import View
from django.shortcuts import render
from login_signup.models.prescription import Prescription
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

decorators = [
    permission_required('login_signup.can_use_medical_stuff', raise_exception=True),
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class RestorePrescriptionView(View):
    template_name = 'home/prescription/restore_prescription.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)

    @staticmethod
    def post(request, **kwargs):
        prescription = Prescription.objects.get(id=kwargs['pk'])
        prescription.is_active = True
        prescription.save()
        return render(request, "home/prescription/restore_prescription_success.html")
