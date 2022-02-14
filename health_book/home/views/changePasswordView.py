from home.forms import PasswordChangingForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


class ChangePasswordView(PasswordChangeView):
    """
    Change the password of the user
    """
    form_class = PasswordChangingForm
    template_name = 'home/change_password.html'
    success_url = reverse_lazy('home:password_success')
