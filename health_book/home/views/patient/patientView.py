from django.views.generic.detail import DetailView
from login_signup.models.customUser import CustomUser
from login_signup.models.notification import Notification
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

decorators = [
    permission_required('login_signup.can_use_medical_stuff', raise_exception=True),
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class PatientView(DetailView):
    model = CustomUser
    template_name = 'home/patient/patient.html'
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.object.first_name + '-' + self.object.last_name
        context['slug'] = slug
        return context

    def dispatch(self, *args, **kwargs):
        id = kwargs.pop('pk', None)
        print(f"{id=}")
        detailedUser = CustomUser.objects.get(id=id)
        notifications = Notification.objects.filter(
            for_user=self.request.user, from_user=detailedUser, notification_type='NP')
        if notifications.exists():
            notifications.delete()

        return super().dispatch(*args, **kwargs)
