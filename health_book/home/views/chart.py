import calendar
import locale
import datetime
from django.views.generic import TemplateView
from django.shortcuts import render
from login_signup.models.doctor import Doctor
from login_signup.models.appointment import Appointment
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

decorators = [
    permission_required('login_signup.can_use_medical_stuff', raise_exception=True),
    login_required(login_url='login')
]


@method_decorator(decorators, name='dispatch')
class ChartView(TemplateView):
    template_name = 'home/chart.html'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.has_perm('login_signup.can_use_medical_stuff'):
            doctor = Doctor.objects.get(user=self.request.user)
            appointments = Appointment.objects.filter(doctor=doctor, is_active=True)
        else:
            appointments = Appointment.objects.filter(user=request.user, is_active=True)

        locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
        days = []
        countDays = {
            'lundi': 0,
            'mardi': 0,
            'mercredi': 0,
            'jeudi': 0,
            'vendredi': 0,
            'samedi': 0,
            'dimanche': 0
        }

        for _appointment in appointments:
            curr_date = _appointment.date
            if datetime.datetime.now().month == curr_date.month:
                days.append(calendar.day_name[curr_date.weekday()])

        for day in days:
            countDays[day] += 1
        context['countDays'] = countDays

        return render(request, self.template_name, context)
