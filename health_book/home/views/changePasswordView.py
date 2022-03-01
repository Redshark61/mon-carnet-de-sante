from home.forms import PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class ChangePasswordView(PasswordChangeView):
    """
    Change the password of the user
    """
    form_class = PasswordChangingForm
    template_name = 'home/change_password.html'
    success_url = reverse_lazy('home:password_success')
