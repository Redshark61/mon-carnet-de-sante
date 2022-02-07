from django.contrib.auth import authenticate, login as loginUser
from django.shortcuts import redirect, render
from django.views import View
from login_signup.models import Job, Doctor, RPPS, CustomUser, Diseases, Treatment
from login_signup.forms import *
# Create your views here.


class IndexView(View):
    template_name = 'login_signup/index.html'

    def render_to_response(self, context, **response_kwargs):
        response = super(IndexView, self).render_to_response(context, **response_kwargs)
        response.set_cookie('medical', False)
        return response

    def get(self, request):
        response = render(request, self.template_name)
        response.set_cookie('medical', False)

        return response

    def post(self, request):
        person, direction = request.POST.get('button').split("&")
        print(person, direction)

        if person == 'personal':
            response = redirect('login') if direction == 'login' else redirect('login_signup:signup', 1)
            response.set_cookie('medical', False)
            return response

        if person == 'medical':
            response = redirect('login') if direction == 'login' else redirect(
                'login_signup:signup', 1)
            response.set_cookie('medical', True)
            return response

        return redirect('login_signup:index')


class SignupView(View):
    template_name = 'login_signup/signup/$.html'

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

    def get(self, request, **kwargs):
        number = kwargs['number']
        context = self.set_context(request, **kwargs)

        if number == 4:
            context['treatments'] = Treatment.objects.all()
            context['diseases'] = Diseases.objects.all()
            context['doctors'] = Doctor.objects.all()
        return render(request, f'login_signup/signup/{number}.html', context)

    def post(self, request, **kwargs):
        number = kwargs['number']
        context = self.set_context(request, **kwargs)
        form = context['form']
        nextNumber = number + 1
        isMedical = request.COOKIES['medical']

        if form.is_valid() or (number == 4 and request.POST.get('doctor') != '') or number == 5:
            if number == 1:
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
            if number == 2:
                request.user.birth_date = form.cleaned_data['birth_date']
                request.user.gender = form.cleaned_data['gender']
                request.user.save()
                if isMedical == 'True':
                    return redirect('home:home')
                return redirect('login_signup:signup', nextNumber)
            if number == 3:
                location = form.save(commit=False)
                location.postal_code = request.POST['postal_code']
                location.save()
                request.user.address = location
                request.user.save()
                return redirect('login_signup:signup', nextNumber)
            if number == 4:
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

                doctor_first_name, doctor_last_name = request.POST['doctor'].split(' - ')
                main_doctor = CustomUser.objects.get(first_name=doctor_first_name, last_name=doctor_last_name)
                request.user.main_doctor = main_doctor
                request.user.save()
                return redirect('login_signup:signup', nextNumber)
            if number == 5:
                print(request.POST)
                if request.POST.get('first_name') != '' and request.POST.get('last_name') != '' and request.POST.get('phone_number') != '':
                    trustedPerson = form.save(commit=False)
                    trustedPerson.user = request.user
                    trustedPerson.save()
                return redirect('login_signup:signup', nextNumber)
            if number == 6:
                return redirect('home:home')
        else:
            print("invalid form : " + str(form.errors))
            context['is_valid'] = False
            return render(request, f'login_signup/signup/{number}.html', context)


class LoginView(View):
    template_name = 'login_signup/login.html'
    form = LoginForm

    @staticmethod
    def deleteField(request, form):
        if request.COOKIES['medical'] == 'True':
            del form.fields['id_code']
            return 'rpps_code', form

        del form.fields['rpps_code']
        return 'id_code', form

    def get(self, request):
        form = self.form()
        _, form = self.deleteField(request, form)
        return render(request, self.template_name, {'form': form, 'is_valid': True})

    def post(self, request):
        form = self.form(request.POST)
        username, form = self.deleteField(request, form)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data[username], password=form.cleaned_data['password'])
            if user is not None:
                loginUser(request, user)
                return redirect('home:home')
            return render(request, 'login_signup/login.html', {'form': form, 'is_valid': False})

        _, form = self.deleteField(request, form)
        return render(request, 'login_signup/login.html', {'is_valid': False, 'form': form})
