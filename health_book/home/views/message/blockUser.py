from django.views import View
from django.shortcuts import render, redirect
from login_signup.models import customUser


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
