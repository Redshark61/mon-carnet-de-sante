from django.views import View
from django.shortcuts import render, redirect
from login_signup.models.diseases import Diseases
from home import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class AddDisease(View):
    """Add a disease to the user"""

    template_name = 'home/diseases/add_disease.html'
    form = forms.AddDiseaseForm

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form(request.POST)
        hasPerm = request.user.has_perm('login_signup.can_use_medical_stuff')
        if form.is_valid() or (hasPerm and request.POST.get('disease', False)):

            if hasPerm:
                disease = request.POST.get('disease')
                Diseases.objects.create(name=disease)
            # Add a disease to the user
            else:
                disease = form.cleaned_data['disease']
                self.request.user.diseases.add(disease)
            return redirect('home:diseases')
        return render(request, self.template_name, {'form': form})
