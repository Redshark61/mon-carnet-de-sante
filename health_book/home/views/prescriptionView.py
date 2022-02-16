from django.views.generic import ListView
from login_signup.models import prescription
from login_signup.models.doctor import Doctor


class PrescriptionView(ListView):
    """
    View for the prescription
    """
    template_name = 'home/prescription.html'
    model = prescription.Prescription

    def get_queryset(self):
        """
        We want to display the appointments for the current user
        """
        queryset = super().get_queryset()
        if self.request.user.has_perm('login_signup.can_use_medical_stuff'):
            print("Doctor")
            doctor = Doctor.objects.get(user=self.request.user)
            userPrescription = queryset.filter(doctor=doctor)
        else:
            userPrescription = queryset.filter(user=self.request.user)
        return userPrescription
