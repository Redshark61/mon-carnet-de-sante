from django.views import View
from django.shortcuts import render, redirect
from login_signup.models.userDisease import UserDisease
from login_signup.models.diseases import Diseases
from home import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class EditDisease(View):
    form = forms.AddDiseaseForm
    template_name = 'home/diseases/edit_disease.html'

    def get(self, request, **kwargs):
        id = kwargs['pk']
        data = {
            'disease': UserDisease.objects.get(id=id).disease
        }
        form = self.form(data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        id = kwargs['pk']
        form = self.form(request.POST)
        if form.is_valid():
            newDisease = form.cleaned_data['disease']
            newDisease = Diseases.objects.get(name=newDisease)
            disease = UserDisease.objects.get(id=id)
            disease.disease = newDisease
            disease.save()
            return redirect('home:diseases')

        return render(request, self.template_name, {'form': form})
