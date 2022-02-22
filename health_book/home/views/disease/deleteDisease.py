from django.views import View
from django.shortcuts import render, redirect
from login_signup.models.userDisease import UserDisease


class DeleteDisease(View):
    """
    Delete the disease from the user
    """
    template_name = 'home/diseases/delete_disease.html'

    def get(self, request, *args, **kwargs):
        """
        Display the confirmation message before deleting the disease
        """
        id = kwargs.get('pk')
        to_be_deleted_disease = UserDisease.objects.get(id=id)
        context = {
            'disease': to_be_deleted_disease
        }
        return render(request, self.template_name, context)

    @staticmethod
    def post(request, *args, **kwargs):
        """
        Actually delete the disease
        """

        id = kwargs.get('pk')
        if request.POST.get('button') == 'delete':
            to_be_deleted_disease = UserDisease.objects.get(id=id)
            to_be_deleted_disease.delete()
            return redirect('home:home')
        return redirect('home:settings')
