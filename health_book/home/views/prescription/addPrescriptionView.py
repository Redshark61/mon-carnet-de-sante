from django.views.generic.edit import FormView
from home import forms
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

decorators = [
    permission_required('login_signup.can_use_medical_stuff', raise_exception=True),
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class AddPrescriptionView(FormView):
    """
    View for the prescription
    """

    template_name = 'home/prescription/add_prescription.html'
    form_class = forms.AddPrescriptionForm
    success_url = reverse_lazy('home:prescription')

    def form_valid(self, form):
        """
        If the form is valid, we save it and redirect to the appointments page
        """
        form.save()
        return super().form_valid(form)
