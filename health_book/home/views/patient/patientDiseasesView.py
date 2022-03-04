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
class PatientDiseasesView(DetailView):
    model = CustomUser
    template_name = 'home/patient/patient_diseases.html'
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        diseases = self.object.diseases.all()
        diseases = [disease.name for disease in diseases]
        prescriptions = Prescription.objects.filter(user=self.object)
        prescriptionDisease = [disease.diseases.name for disease in prescriptions]
        for disease in prescriptionDisease:
            diseases.append(disease)
        # transform list of diseases into a set to remove duplicates
        diseases = set(diseases)
        print(diseases)
        context['diseases'] = diseases
        return context
