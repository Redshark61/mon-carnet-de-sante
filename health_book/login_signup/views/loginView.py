from django.contrib.auth import authenticate, login as loginUser
from django.shortcuts import redirect, render
from login_signup.forms import LoginForm
from login_signup.views.indexView import IndexView


class LoginView(IndexView):
    """
    Login page.
    Inherits from IndexView to get the `redirect_to_signup` method.
    """

    template_name = 'login_signup/login.html'
    form = LoginForm

    @staticmethod
    def deleteField(request, form):
        """
        Delete the `RPPS` field from the form if the user is a medical user,
        else delete the `id_code` field.
        """

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
        # The username here is in fact the rpps or social security number
        username, form = self.deleteField(request, form)

        inputs = [input for input in request.POST]

        if 'login' in inputs:
            # Redirect to the right page weither it's a medical user or not
            response = super().redirect_to_signup(request)
            return response

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data[username], password=form.cleaned_data['password'])
            if user is not None:
                loginUser(request, user)
                return redirect('home:home')
            return render(request, 'login_signup/login.html', {'form': form, 'is_valid': False})

        _, form = self.deleteField(request, form)
        return render(request, 'login_signup/login.html', {'is_valid': False, 'form': form})
