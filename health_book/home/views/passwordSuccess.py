from django.shortcuts import render


def passwordSuccess(request):
    """
    Successful password change
    """
    return render(request, 'home/password_success.html')
