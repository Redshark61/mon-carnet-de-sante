import datetime
from django.views.generic import ListView
from login_signup.models import prescription
from login_signup.models.doctor import Doctor


class PrescriptionView(ListView):
    """
    View for the prescription
    """
    template_name = 'home/prescription.html'
    model = prescription.Prescription
    isFilter = False

    def get_context_data(self, **kwargs):
        """
        We want to display the prescription for the current user
        """
        context = super().get_context_data(**kwargs)
        context['isFilter'] = self.isFilter
        return context

    def post(self, request, *args, **kwargs):
        """
        If the user wants to display the past prescriptions
        """
        self.isFilter = request.POST.get('displayPast')
        print("post", self.isFilter)
        return self.get(request, *args, **kwargs)

    def get_queryset(self):
        """
        We want to display the prescription for the current user
        """
        queryset = super().get_queryset()
        if self.request.user.has_perm('login_signup.can_use_medical_stuff'):
            print("Doctor")
            doctor = Doctor.objects.get(user=self.request.user)
            userPrescription = queryset.filter(doctor=doctor)
        else:
            userPrescription = queryset.filter(user=self.request.user)

        if not self.isFilter:
            userPrescription = userPrescription.filter(is_active=True)

            for prescription in userPrescription:
                if not prescription.is_permanent and (prescription.end_date < datetime.date.today()):
                    prescription.is_active = False
                    prescription.save()
                else:
                    prescription.is_active = True
                    prescription.save()

        return userPrescription
