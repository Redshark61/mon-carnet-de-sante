from django.views import View
from django.shortcuts import render, redirect
from home import forms


class AddTreatment(View):
    """Add a treatment to the user"""
    template_name = 'home/add_treatment.html'
    form = forms.AddTreatmentForm

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            treatment = form.cleaned_data['treatment']
            self.request.user.treatments.add(treatment)
            return redirect('home:treatments')
        return render(request, self.template_name, {'form': form})
