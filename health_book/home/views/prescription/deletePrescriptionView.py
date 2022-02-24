from django.views import View
from django.shortcuts import render
from login_signup.models.prescription import Prescription


class DeletePrescriptionView(View):
    template_name = 'home/prescription/delete_prescription.html'

    def get(self, request, **kwargs):
        prescription = Prescription.objects.get(id=kwargs['pk'])
        context = {
            'prescription': prescription
        }
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        prescription = Prescription.objects.get(id=kwargs['pk'])
        prescription.is_active = False
        prescription.save()
        return render(request, 'home/prescription/delete_prescription_success.html')
