from django.views import View
from login_signup.models.job import Job
from login_signup.models.doctor import Doctor
from login_signup.models.rpps import RPPS
from login_signup.models.customUser import CustomUser
from login_signup.models.diseases import Diseases
from login_signup.models.treatment import Treatment
from django.shortcuts import redirect, render
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import login as loginUser
from login_signup.forms import *


class SignupView(View):
    number = 1
    template_name = f'login_signup/signup/{number}.html'

    @staticmethod
    def set_context(request, **kwargs):
        number = kwargs['number']
        className = eval(f"Connection{number}")
        nextNumber = number + 1
        previousNumber = number - 1
        isMedical = request.COOKIES['medical']
        stepProgress = '12' if isMedical == 'True' else '123456'
        jobs = Job.objects.all() if number == 1 else None
        context = {
            'next_id': nextNumber,
            'current_id': str(number),
            'prev_id': previousNumber,
            'is_medical': True if isMedical == 'True' else False,
            'step_progress': stepProgress,
            'is_valid': True,
            'jobs': jobs,
        }

        form = className.__call__(request.POST or None)
        context['form'] = form
        return context

    def dispatch(self, request, *args, **kwargs):
        self.number = kwargs['number']
        return super(SignupView, self).dispatch(request, *args, **kwargs)

    def get(self, request, **kwargs):
        context = self.set_context(request, **kwargs)

        if self.number == 4:
            context['treatments'] = Treatment.objects.all()
            context['diseases'] = Diseases.objects.all()
            context['doctors'] = Doctor.objects.all()
        return render(request, f'login_signup/signup/{self.number}.html', context)

    def post(self, request, **kwargs):
        context = self.set_context(request, **kwargs)
        form = context['form']
        nextNumber = self.number + 1
        isMedical = request.COOKIES['medical']

        if form.is_valid() or (self.number == 4 and request.POST.get('doctor') != '') or self.number == 5:
            if self.number == 1:
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']
                username = request.POST['code_id']

                if username == '':
                    context['is_valid'] = False
                    return render(request, f'login_signup/signup/{self.number}.html', context)
                # check if the password is valid
                error = ''
                try:
                    validate_password(password)
                except ValidationError as e:
                    error = e.messages
                    context['is_valid'] = False
                    context['errors'] = error
                    return render(request, f'login_signup/signup/{self.number}.html', context)
                if password != confirm_password:
                    context['is_valid'] = False
                    context['errors'] = ['Les mots de passe ne correspondent pas']
                    return render(request, f'login_signup/signup/{self.number}.html', context)
                user = CustomUser.objects.create_user(
                    username=request.POST['code_id'],
                    email=form.cleaned_data['mail'],
                    password=form.cleaned_data['password'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'])
                user.save()
                if isMedical == 'True':
                    job = Job.objects.get(name=request.POST['job'])
                    rpps = RPPS.objects.get(rpps=request.POST['code_id'])
                    doctor = Doctor(user=user,
                                    rpps=rpps,
                                    job=job)
                    doctor.save()
                loginUser(request, user)
                return redirect('login_signup:signup', nextNumber)
            if self.number == 2:
                request.user.birth_date = form.cleaned_data['birth_date']
                request.user.gender = form.cleaned_data['gender']
                request.user.save()
                if isMedical == 'True':
                    return redirect('home:home')
                return redirect('login_signup:signup', nextNumber)
            if self.number == 3:
                location = form.save(commit=False)
                location.user = request.user
                location.save()
                return redirect('login_signup:signup', nextNumber)
            if self.number == 4:
                treatments = {key: value for key, value in request.POST.items()
                              if 'treatment' in key and value != ''}
                diseases = {key: value for key, value in request.POST.items()
                            if 'disease' in key and value != ''}
                for treatment in treatments:
                    treatment = Treatment.objects.get(name=treatments[treatment])
                    request.user.treatments.add(treatment)

                for disease in diseases:
                    disease = Diseases.objects.get(name=diseases[disease])
                    request.user.diseases.add(disease)

                doctor_first_name, doctor_last_name = request.POST['doctor'].split()
                doctor_user = CustomUser.objects.get(
                    first_name=doctor_first_name, last_name=doctor_last_name)

                main_doctor = Doctor.objects.get(user=doctor_user)
                request.user.main_doctor = main_doctor
                request.user.save()
                return redirect('login_signup:signup', nextNumber)
            if self.number == 5:
                print(request.POST)
                if request.POST.get('first_name') != '' and request.POST.get('last_name') != '' and request.POST.get('phone_number') != '':
                    trustedPerson = form.save(commit=False)
                    trustedPerson.user = request.user
                    trustedPerson.save()
                return redirect('login_signup:signup', nextNumber)
            if self.number == 6:
                return redirect('home:home')
        else:
            print("invalid form : " + str(form.errors))
            context['is_valid'] = False
            return render(request, f'login_signup/signup/{self.number}.html', context)
