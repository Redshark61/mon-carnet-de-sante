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
        """
        The get_queryset() method is called when the view is used to retrieve data.
        The super() method is used to call the get_queryset() method of the parent class.
        The filter() method is used to filter the queryset based on the User_treatment field.
        The filter() method is used to filter the queryset based on the is_active field.
        The return statement returns the filtered queryset
        """
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

    def get_context_data(self, **kwargs) -> dict:
        """
        This function is called when the view is rendered. It adds the prescriptions and treatments to the
        context dictionary
        """
        context = super().get_context_data(**kwargs)
        context['prescriptions'] = Prescription.objects.filter(user=self.request.user)
        context['treatments'] = Treatment.objects.all()
        context['isFilter'] = self.isFilter
        return context
