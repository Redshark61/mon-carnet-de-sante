from django.views.generic.list import ListView
from login_signup.models.customUser import CustomUser
from login_signup.models.doctor import Doctor


class PatientsView(ListView):
    model = CustomUser
    template_name = 'home/patient/patients.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        me = Doctor.objects.get(user=self.request.user)
        myPatient = queryset.filter(main_doctor=me)
        return myPatient
