from django.views import View
from django.shortcuts import render, redirect
from login_signup.models.treatment import Treatment


class DeleteTreatment(View):
    template_name = 'home/delete_treatment.html'

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        treatment = Treatment.objects.get(id=id)
        context = {
            'treatment': treatment
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        if request.POST.get('button') == 'delete':
            treatment = Treatment.objects.get(id=id)
            self.request.user.treatments.remove(treatment)
        return redirect('home:treatments')
