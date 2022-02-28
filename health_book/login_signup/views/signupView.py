from django.views import View
from login_signup.models.job import Job
from login_signup.models.doctor import Doctor
from login_signup.models.rpps import RPPS
from login_signup.models.customUser import CustomUser
from login_signup.models.diseases import Diseases
from login_signup.models.notification import Notification
from login_signup.models.treatment import Treatment
from django.shortcuts import redirect, render
from django.contrib.auth.models import Permission
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import login as loginUser
from login_signup.forms import *


class SignupView(View):
    """
    All the signup pages
    """

    number = 1
    template_name = f'login_signup/signup/{number}.html'

    @staticmethod
    def set_context(request, **kwargs):
        """
        Set the context for the current page as well as the form
        """
        number = kwargs['number']
        className = eval(f"Connection{number}")
        nextNumber = number + 1
        previousNumber = number - 1
        isMedical = request.COOKIES['medical']
        # If the user is a medical user he won't fill the page 3 to 6
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
        """
        Set the current progression in the signup process by getting the number of the current page
        """
        self.number = kwargs['number']
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, **kwargs):
        context = self.set_context(request, **kwargs)
        if request.user.is_authenticated:
            if kwargs['number'] != request.user.current_signup_progress:
                return redirect(f'/signup/{request.user.current_signup_progress}')
        else:
            if kwargs['number'] != 1:
                return redirect('/signup/1')

        if self.number == 4:
            # Those fields are populated directly in the template
            context['treatments'] = Treatment.objects.all()
            context['diseases'] = Diseases.objects.all()
            context['doctors'] = Doctor.objects.all()
        return render(request, f'login_signup/signup/{self.number}.html', context)

    def post(self, request, **kwargs):
        context = self.set_context(request, **kwargs)
        form = context['form']
        nextNumber = self.number + 1
        isMedical = request.COOKIES['medical']

        # For the 4th page the user doesn't need to fill all the fields except the main doctor
        # For the 5th page the user doesn't need to fill the fields
        if form.is_valid() or (self.number == 4 and request.POST.get('doctor') != '') or self.number == 5:
            if request.user.is_authenticated:
                request.user.current_signup_progress = nextNumber
                request.user.save()

            if self.number == 1:
                password = form.cleaned_data['password']
                confirm_password = form.cleaned_data['confirm_password']
                username = request.POST['code_id']

                # Username being a handmade field, Django don't check its nulleness. We need to do it ourselves
                if username == '':
                    context['is_valid'] = False
                    return render(request, f'login_signup/signup/{self.number}.html', context)

                # check if the password is valid
                error = ''
                try:
                    validate_password(password)
                except ValidationError as e:
                    # If the password is not valid, we get the error message
                    # and we display it in the template
                    error = e.messages
                    context['is_valid'] = False
                    context['errors'] = error
                    return render(request, f'login_signup/signup/{self.number}.html', context)

                # check if the password and the confirmation are the same
                if password != confirm_password:
                    context['is_valid'] = False
                    context['errors'] = ['Les mots de passe ne correspondent pas']
                    return render(request, f'login_signup/signup/{self.number}.html', context)

                # check if the username is already used
                if CustomUser.objects.filter(username=username).exists():
                    context['is_valid'] = False
                    context['errors'] = ['Ce code est déjà utilisé']
                    return render(request, f'login_signup/signup/{self.number}.html', context)

                # If everything is valid, we create the user
                user = CustomUser.objects.create_user(
                    username=request.POST['code_id'],
                    email=form.cleaned_data['mail'],
                    password=form.cleaned_data['password'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    role="PATIENT" if isMedical == 'False' else "MEDICAL_USER",
                    current_signup_progress=nextNumber,
                )
                if isMedical == 'True':
                    permission = Permission.objects.get(codename='can_use_medical_stuff')
                    user.user_permissions.add(permission)
                user.save()

                # If the user is a medical user, we create the Doctor object
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
                # Add the fileds birth_date and phone_number to the user
                request.user.birth_date = form.cleaned_data['birth_date']
                request.user.gender = form.cleaned_data['gender']
                request.user.current_signup_progress = nextNumber
                request.user.save()

                # If the user is a medical user, we redirect it to the main page
                if isMedical == 'True':
                    return redirect('home:home')
                return redirect('login_signup:signup', nextNumber)
            if self.number == 3:
                # Save the location of the user
                location = form.save(commit=False)
                location.user = request.user
                location.postal_code = request.POST.get('postal_code')
                location.save()
                request.user.current_signup_progress = nextNumber
                request.user.save()
                return redirect('login_signup:signup', nextNumber)
            if self.number == 4:

                # All the treatments / diseases / doctors are saved in the database and handled in js

                # Get all the treatments
                treatments = {key: value for key, value in request.POST.items()
                              if 'treatment' in key and value != ''}
                diseases = {key: value for key, value in request.POST.items()
                            if 'disease' in key and value != ''}

                # For each treatment, we create a Treatment object and add it to the user
                for treatment in treatments:
                    treatment = Treatment.objects.get(name=treatments[treatment])
                    request.user.treatments.add(treatment)

                # For each disease, we create a Disease object and add it to the user
                for disease in diseases:
                    disease = Diseases.objects.get(name=diseases[disease])
                    request.user.diseases.add(disease)

                # Get the main doctor
                doctor_first_name, doctor_last_name = request.POST['doctor'].split()
                doctor_user = CustomUser.objects.get(
                    first_name=doctor_first_name, last_name=doctor_last_name)
                main_doctor = Doctor.objects.get(user=doctor_user)
                request.user.main_doctor = main_doctor
                Notification.objects.create(
                    for_user=main_doctor.user,
                    from_user=request.user,
                    notification_type="NP"
                )
                request.user.current_signup_progress = nextNumber
                request.user.save()
                return redirect('login_signup:signup', nextNumber)
            if self.number == 5:
                # add the trusted person to the user
                try:
                    trustedPerson = form.save(commit=False)
                except ValueError:
                    return redirect('login_signup:signup', nextNumber)
                trustedPerson.user = request.user
                trustedPerson.save()
                request.user.current_signup_progress = nextNumber
                request.user.save()
                return redirect('login_signup:signup', nextNumber)
            if self.number == 6:
                return redirect('home:home')
        else:
            context['is_valid'] = False
            return render(request, f'login_signup/signup/{self.number}.html', context)
