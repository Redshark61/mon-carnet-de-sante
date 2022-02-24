from django.views import View
from django.shortcuts import render, redirect
from login_signup.models.treatment import Treatment


class DeleteTreatment(View):
    """
    Delete the treatment from the user
    """
    template_name = 'home/treatment/delete_treatment.html'

    def get(self, request, *args, **kwargs):
        """
        Display the confirmation message before deleting the treatment
        """
        id = kwargs.get('pk')
        treatment = Treatment.objects.get(id=id)
        context = {
            'treatment': treatment
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """
        Actually delete the treatment
        """

        id = kwargs.get('pk')
        if request.POST.get('button') == 'delete':
            treatment = Treatment.objects.get(id=id)
            treatment = self.request.user.treatments.get(name=treatment)
            treatment.is_active = False
            treatment.save()
        return redirect('home:treatments')
