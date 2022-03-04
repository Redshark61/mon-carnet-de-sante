from django.views.generic.list import ListView
from login_signup.models.treatment import Treatment
from login_signup.models.prescription import Prescription
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class TreatmentsView(ListView):
    """
    Display the treatments for the current user
    """

    model = Treatment
    template_name = 'home/treatment/treatments.html'
    isFilter = False

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.isFilter:
            userTreatments = queryset.filter(User_treatment=self.request.user)
        else:
            userTreatments = queryset.filter(User_treatment=self.request.user, is_active=True)

        return userTreatments

    def post(self, request, *args, **kwargs):
        """
        If the user wants to display the past prescriptions
        """
        self.isFilter = request.POST.get('displayPast')
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prescriptions'] = Prescription.objects.filter(user=self.request.user)
        context['treatments'] = Treatment.objects.all()
        context['isFilter'] = self.isFilter
        return context
