from django.views.generic.detail import DetailView
from login_signup.models.customUser import CustomUser
from login_signup.models.prescription import Prescription


class PatientTreatmentsView(DetailView):
    model = CustomUser
    template_name = 'home/patient_treatments.html'
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
