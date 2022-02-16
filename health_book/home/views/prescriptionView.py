from django.shortcuts import render, redirect
from django.views import View


class PrescriptionView(View):
    """
    View for the prescription
    """
    template_name = 'home/prescription.html'

    def get(self, request):
        """
        Display the prescription
        """
        return render(request, self.template_name)

    def post(self, request):
        """
        Save the prescription
        """
        return redirect('home:prescription')
