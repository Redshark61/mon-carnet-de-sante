from django.views.generic.list import ListView
from login_signup.models.userDisease import UserDisease
from login_signup.models.prescription import Prescription
from login_signup.models.diseases import Diseases


class DiseasesView(ListView):
    model = UserDisease
    template_name = 'home/diseases.html'

    def get_queryset(self):
        """
        Display the diseases for the current user
        """
        queryset = super().get_queryset()
        userDiseases = queryset.filter(user=self.request.user)
        print(userDiseases)
        return userDiseases

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prescriptions'] = Prescription.objects.filter(user=self.request.user)
        context['diseases'] = Diseases.objects.all()
        return context
