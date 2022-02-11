from django.shortcuts import render


def passwordSuccess(request):
    return render(request, 'home/password_success.html')
