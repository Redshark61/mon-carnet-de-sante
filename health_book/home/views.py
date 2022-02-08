from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from login_signup.models import UserDisease


@method_decorator(login_required(login_url='index'), name="get")
class HomeView(View):
    template_name = 'home/home.html'

    def get(self, request):
        context = {
            'user': request.user
        }

        return render(request, self.template_name, context)


class DiseasesView(ListView):
    model = UserDisease
    template_name = 'home/diseases.html'
    # context_object_name = 'disease_list'

    def get_queryset(self):
        queryset = super(DiseasesView, self).get_queryset()
        userDiseases = queryset.filter(user=self.request.user)
        # # print(userDiseases.get(username=self.request.user))
        print(userDiseases)
        return userDiseases
