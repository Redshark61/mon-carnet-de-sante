from django.views import View
from django.shortcuts import render, redirect
from login_signup.models.userDisease import UserDisease


class DeleteDisease(View):
    template_name = 'home/delete_disease.html'

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        to_be_deleted_disease = UserDisease.objects.get(id=id)
        context = {
            'disease': to_be_deleted_disease
        }
        return render(request, self.template_name, context)

    @staticmethod
    def post(request, *args, **kwargs):
        id = kwargs.get('pk')
        if request.POST.get('button') == 'delete':
            to_be_deleted_disease = UserDisease.objects.get(id=id)
            to_be_deleted_disease.delete()
            return redirect('home:home')
        return redirect('home:settings')
