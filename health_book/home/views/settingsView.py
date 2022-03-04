from django.views import View
from home.forms import UserForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class SettingsView(View):
    """
    View to change the user's settings
    """
    template_name = 'home/settings.html'

    def get(self, request):
        """
        Display the settings form
        """
        form = UserForm(instance=request.user)

        context = {
            'user': request.user,
            'form': form,
            'is_medical': request.COOKIES.get('is_medical'),
            'is_valid': True
        }

        return render(request, self.template_name, context)

    def post(self, request):
        """
        Actually change the settings
        """

        # check whether the button clicked had the value delete or not
        if request.POST.get('button') == 'delete':
            return redirect('home:delete')
        else:
            form = UserForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('home:settings')
            context = {
                'form': form,
                'is_valid': False
            }
            return render(request, self.template_name, context)
