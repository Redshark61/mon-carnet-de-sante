from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def passwordSuccess(request):
    """
    Successful password change
    """
    return render(request, 'home/password_success.html')
