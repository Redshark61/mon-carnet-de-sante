from django.views.generic.edit import FormView
from home import forms
from django.urls import reverse_lazy


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
