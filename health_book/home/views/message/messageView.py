from django.views import View
from django.shortcuts import render, redirect
from login_signup.models import doctor, customUser, message


class MessageView(View):
    template_name = 'home/message.html'

    def get(self, request, **kwargs):
        slug = kwargs['slug']
        first_name, last_name = slug.split('-')
        # Get the user's messages
        user = customUser.CustomUser.objects.get(first_name=first_name, last_name=last_name)
        if request.user.has_perm('login_signup.can_use_medical_stuff'):
            # Get the doctor's messages
            doctorUser = doctor.Doctor.objects.get(user=request.user)
            messages = message.Message.objects.filter(doctor=doctorUser, user=user)
        else:
            doctorUser = doctor.Doctor.objects.get(user=user)
            messages = message.Message.objects.filter(user=request.user, doctor=doctorUser)

        context = {
            'messages': messages,
            'userChat': user,
            'slug': slug,
        }

        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        slug = kwargs['slug']
        first_name, last_name = slug.split('-')
        # Get the user's messages
        user = slugUser = customUser.CustomUser.objects.get(first_name=first_name, last_name=last_name)
        if request.user.has_perm('login_signup.can_use_medical_stuff'):
            doctorUser = doctor.Doctor.objects.get(user=request.user)
        else:
            doctorUser = doctor.Doctor.objects.get(user=user)
            user = request.user

        message.Message.objects.create(
            user=user,
            doctor=doctorUser,
            message=request.POST.get('message'),
            sender=request.user,
            destination=slugUser,
        )

        return redirect('home:message', slug=slug)
