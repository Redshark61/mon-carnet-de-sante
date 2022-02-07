from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.decorators import method_decorator


@method_decorator(login_required(login_url='index'), name="get")
class HomeView(View):
    template_name = 'home/home.html'

    def get(self, request):
        context = {
            'user': request.user
        }

        return render(request, self.template_name, context)
