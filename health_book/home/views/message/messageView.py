from django.views import View
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from login_signup.models import doctor, customUser, message, notification
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

decorators = [
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
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

        onWaitingNotifications = notification.Notification.objects.filter(
            for_user=request.user, from_user=user, notification_type='M')
        onWaitingNotifications.delete()

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

        try:
            previousNotif = notification.Notification.objects.get(
                from_user=request.user, for_user=slugUser, notification_type='M')
        except ObjectDoesNotExist:
            notification.Notification.objects.create(
                from_user=request.user, for_user=slugUser, notification_type='M')

        message.Message.objects.create(
            user=user,
            doctor=doctorUser,
            message=request.POST.get('message'),
            sender=request.user,
            destination=slugUser,
        )

        return redirect('home:message', slug=slug)
