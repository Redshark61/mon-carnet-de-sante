from django.views.generic.detail import DetailView
from login_signup.models.customUser import CustomUser


class PatientView(DetailView):
    model = CustomUser
    template_name = 'home/patient.html'
    context_object_name = 'patient'
