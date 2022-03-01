from django.views import View
from django.shortcuts import render, redirect
from login_signup.models import customUser
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

decorators = [
    permission_required('login_signup.can_use_medical_stuff', raise_exception=True),
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class BlockUser(View):
    template_name = 'home/blockUser.html'

    def get(self, request, *args, **kwargs):
        slug = kwargs.pop('slug')
        first_name, last_name = slug.split('-')
        user = customUser.CustomUser.objects.get(first_name=first_name, last_name=last_name)
        context = {
            'userToBlock': user,
            'slug': slug,
        }
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        slug = kwargs.pop('slug')
        first_name, last_name = slug.split('-')
        user = customUser.CustomUser.objects.get(first_name=first_name, last_name=last_name)
        request.user.blocked_user.add(user)
        request.user.save()
        return redirect('home:messages')
