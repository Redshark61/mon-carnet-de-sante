from django.views.generic.detail import DetailView
from login_signup.models.customUser import CustomUser


class PatientView(DetailView):
    model = CustomUser
    template_name = 'home/patient/patient.html'
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.object.first_name + '-' + self.object.last_name
        context['slug'] = slug
        return context
