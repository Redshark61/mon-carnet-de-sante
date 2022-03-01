from django.views.generic.detail import DetailView
from login_signup.models.customUser import CustomUser
from login_signup.models.prescription import Prescription
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

decorators = [
    permission_required('login_signup.can_use_medical_stuff', raise_exception=True),
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class PatientTreatmentsView(DetailView):
    model = CustomUser
    template_name = 'home/patient/patient_treatments.html'
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        treatments = self.object.treatments.all()
        treatments = [treatment.name for treatment in treatments]
        prescriptions = Prescription.objects.filter(user=self.object)
        prescriptionDisease = [treatment.treatment.name for treatment in prescriptions]
        for treatment in prescriptionDisease:
            treatments.append(treatment)
        # transform list of treatments into a set to remove duplicates
        treatments = set(treatments)
        print(treatments)
        context['treatments'] = treatments
        return context
