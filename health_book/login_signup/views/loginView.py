from django.contrib.auth import authenticate, login as loginUser
from django.shortcuts import redirect, render
from login_signup.forms import LoginForm
from login_signup.views.indexView import IndexView


class LoginView(IndexView):
    template_name = 'login_signup/login.html'
    form = LoginForm

    @staticmethod
    def deleteField(request, form):
        if request.COOKIES['medical'] == 'True':
            del form.fields['id_code']
            return 'rpps_code', form

        del form.fields['rpps_code']
        return 'id_code', form

    def get(self, request):
        form = self.form()
        _, form = self.deleteField(request, form)
        return render(request, self.template_name, {'form': form, 'is_valid': True})

    def post(self, request):
        form = self.form(request.POST)
        username, form = self.deleteField(request, form)

        inputs = [input for input in request.POST]
        if 'login' in inputs:
            print("its login")
            print(request.POST.get('button'))
            response = super().redirect_to_signup(request)
            return response
        else:

            if form.is_valid():
                user = authenticate(
                    username=form.cleaned_data[username], password=form.cleaned_data['password'])
                if user is not None:
                    loginUser(request, user)
                    return redirect('home:home')
                return render(request, 'login_signup/login.html', {'form': form, 'is_valid': False})

            _, form = self.deleteField(request, form)
            return render(request, 'login_signup/login.html', {'is_valid': False, 'form': form})
