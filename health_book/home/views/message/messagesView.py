from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.db.models import Q
from login_signup.models import customUser, message, doctor, notification
from home.forms import CreateNewMessageForm


class MessagesView(FormView):
    form_class = CreateNewMessageForm
    template_name = 'home/messages.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.request.user.has_perm('login_signup.can_use_medical_stuff'):
            # Get the doctor's messages
            user = doctor.Doctor.objects.get(user=self.request.user)
            messages = message.Message.objects.filter(doctor=user)
            # Filter in order to remove the duplicates among the user's messages
            # userName return a list of user's id
            userName = messages.values_list('user', flat=True)
            # get all the customUser
            userNames = customUser.CustomUser.objects.filter(
                Q(id__in=userName) & ~Q(blocked_user__in=[self.request.user]))
            # Transform first_name and last_name into a slug
            slugName = [(f"{name.first_name} {name.last_name}").replace(' ', '-') for name in userNames]
        else:
            messages = message.Message.objects.filter(user=self.request.user)
            userName = messages.values_list('doctor', flat=True)
            userNames = doctor.Doctor.objects.filter(id__in=userName)
            slugName = [(f"{name.user.first_name} {name.user.last_name}").replace(' ', '-')
                        for name in userNames]

        onWaitingNotifications = notification.Notification.objects.filter(for_user=self.request.user)

        context["zipped"] = zip(userNames, slugName)
        if onWaitingNotifications.exists():
            context["notifications"] = [str(notification.from_user)
                                        for notification in onWaitingNotifications]

        return context

    def form_valid(self, form):
        destination = self.request.POST.get('destination')
        user = customUser.CustomUser.objects.get(id=destination)
        user = user.first_name + '-' + user.last_name
        destination = user
        return redirect('home:message', slug=destination)
