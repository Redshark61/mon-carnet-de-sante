from django.views import View
from home.forms import UserForm
from django.shortcuts import render, redirect


class SettingsView(View):
    template_name = 'home/settings.html'

    def get(self, request):
        form = UserForm(instance=request.user)

        context = {
            'user': request.user,
            'form': form,
            'is_medical': request.COOKIES.get('is_medical'),
            'is_valid': True
        }

        return render(request, self.template_name, context)

    def post(self, request):
        # check whether the button clicked had the value delete or not
        if request.POST.get('button') == 'delete':
            return redirect('home:delete')
        else:
            form = UserForm(request.POST, instance=request.user)
            print(form.errors)
            print(form.cleaned_data)
            print(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home:settings')
            context = {
                'form': form,
                'is_valid': False
            }
            return render(request, self.template_name, context)
