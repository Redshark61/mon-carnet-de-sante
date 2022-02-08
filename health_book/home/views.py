from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from login_signup.models import Treatment
from login_signup.models import UserDisease
from . import forms


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


class TreatmentsView(ListView):
    model = Treatment
    template_name = 'home/treatments.html'

    def get_queryset(self):
        queryset = super(TreatmentsView, self).get_queryset()
        userTreatments = queryset.filter(User_treatment=self.request.user)
        print(userTreatments)
        return userTreatments


class SettingsView(View):
    template_name = 'home/settings.html'
    form = forms.UserForm

    def get(self, request):
        form = self.form(instance=self.request.user)
        context = {
            'user': request.user,
            'form': form,
            'is_medical': request.COOKIES.get('is_medical')
        }

        return render(request, self.template_name, context)
