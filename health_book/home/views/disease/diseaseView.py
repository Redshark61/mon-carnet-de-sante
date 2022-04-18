from django.views.generic.list import ListView
from login_signup.models.userDisease import UserDisease
from login_signup.models.prescription import Prescription
from login_signup.models.diseases import Diseases
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class DiseasesView(ListView):
    """
    Display the diseases for the current user
    """

    model = UserDisease
    template_name = 'home/diseases/diseases.html'
    isFilter = True

    def get_queryset(self):
        """
        Display the diseases for the current user
        """
        queryset = super().get_queryset()
        if self.isFilter:
            prescriptions = Prescription.objects.filter(user=self.request.user)
            userDiseases = queryset.filter(user=self.request.user)
        else:
            prescriptions = Prescription.objects.filter(user=self.request.user, is_active=True)
            userDiseases = queryset.filter(user=self.request.user, is_active=True)
        return (userDiseases, prescriptions)

    def post(self, request, *args, **kwargs):
        """
        If the user wants to display the past prescriptions
        """
        self.isFilter = request.POST.get('displayPast')
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['prescriptions'] = Prescription.objects.filter(user=self.request.user)
        context['diseases'] = Diseases.objects.all()
        context['isFilter'] = self.isFilter
        return context
