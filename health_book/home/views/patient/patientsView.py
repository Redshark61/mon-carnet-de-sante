from django.views.generic.list import ListView
from login_signup.models.customUser import CustomUser
from login_signup.models.doctor import Doctor
from login_signup.models.notification import Notification
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

decorators = [
    permission_required('login_signup.can_use_medical_stuff', raise_exception=True),
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class PatientsView(ListView):
    model = CustomUser
    template_name = 'home/patient/patients.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notifications = Notification.objects.filter(
            for_user=self.request.user, notification_type='NP')
        notificationUser = notifications.values_list('from_user')
        context['notifications'] = []

        for user in notificationUser:
            context['notifications'].append(CustomUser.objects.get(id=user[0]))

        print(f"{context['notifications']=}")
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        me = Doctor.objects.get(user=self.request.user)
        myPatient = queryset.filter(main_doctor=me)
        return myPatient
