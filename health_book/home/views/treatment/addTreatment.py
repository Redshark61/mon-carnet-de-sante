from django.views import View
from django.shortcuts import render, redirect
from home import forms
from login_signup.models.treatment import Treatment
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class AddTreatment(View):
    """Add a treatment to the user"""
    template_name = 'home/treatment/add_treatment.html'
    form = forms.AddTreatmentForm

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form(request.POST)
        hasPerm = request.user.has_perm('login_signup.can_use_medical_stuff')

        if form.is_valid() or (hasPerm and request.POST.get('treatment', False)):

            if hasPerm:
                treatment = request.POST.get('treatment')
                Treatment.objects.create(name=treatment)
            else:
                treatment = form.cleaned_data['treatment']
                self.request.user.treatments.add(treatment)
            return redirect('home:treatments')
        return render(request, self.template_name, {'form': form})
