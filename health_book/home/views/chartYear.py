import calendar
import locale
import datetime
from django.views.generic import TemplateView
from django.shortcuts import render
from login_signup.models.appointment import Appointment
from login_signup.models.doctor import Doctor
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

decorators = [
    permission_required('login_signup.can_use_medical_stuff', raise_exception=True),
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class ChartYearView(TemplateView):
    template_name = 'home/chartYear.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.has_perm('login_signup.can_use_medical_stuff'):
            doctor = Doctor.objects.get(user=self.request.user)
            appointments = Appointment.objects.filter(doctor=doctor, is_active=True)
        else:
            appointments = Appointment.objects.filter(user=request.user, is_active=True)
        locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
        months = []
        countMonths = {
            'janvier': 0,
            'février': 0,
            'mars': 0,
            'avril': 0,
            'mai': 0,
            'juin': 0,
            'juillet': 0,
            'août': 0,
            'septembre': 0,
            'octobre': 0,
            'novembre': 0,
            'décembre': 0,
        }

        for _appointment in appointments:
            curr_date = _appointment.date
            if datetime.datetime.now().year == curr_date.year:
                months.append(calendar.month_name[curr_date.month])

        for month in months:
            countMonths[month] += 1

        context['countMonths'] = countMonths

        return render(request, self.template_name, context)
