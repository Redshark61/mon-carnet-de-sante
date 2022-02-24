from django.shortcuts import render, redirect
from django.views import View
from home import forms
from login_signup.models.treatment import Treatment


class EditTreatment(View):
    form = forms.AddTreatmentForm
    template_name = 'home/treatment/edit_treatment.html'

    def get(self, request, **kwargs):
        id = kwargs['pk']
        data = {
            'treatment': Treatment.objects.get(id=id)
        }
        print(data)
        form = self.form(data)
        print(form)
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        id = kwargs['pk']
        form = self.form(request.POST)
        if form.is_valid():
            oldTreatment = request.user.treatments.get(id=id)
            request.user.treatments.remove(oldTreatment)
            newTreatment = form.cleaned_data['treatment']
            newTreatment = Treatment.objects.get(name=newTreatment)
            request.user.treatments.add(newTreatment)
            return redirect('home:treatments')

        return render(request, self.template_name, {'form': form})
