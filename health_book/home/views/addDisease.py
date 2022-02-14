from django.views import View
from django.shortcuts import render, redirect
from home import forms


class AddDisease(View):
    """Add a disease to the user"""

    template_name = 'home/add_disease.html'
    form = forms.AddDiseaseForm

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():

            # Add a disease to the user
            disease = form.cleaned_data['disease']
            self.request.user.diseases.add(disease)
            return redirect('home:diseases')
        return render(request, self.template_name, {'form': form})
