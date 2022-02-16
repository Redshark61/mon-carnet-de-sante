from django import forms
from login_signup.models.customUser import CustomUser
from login_signup.models import diseases, treatment, appointment, prescription
from django.contrib.auth.forms import PasswordChangeForm


class UserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'gender',
            'first_name',
            'last_name',
            'main_doctor',
            #   'parent1',
            #   'parent2',
            'birth_date',
        )
        labels = {
            'username': 'Nom d\'utilisateur',
            'email': 'Adresse email',
            'gender': 'Sexe',
            'first_name': 'Prénom',
            'last_name': 'Nom de famille',
            'main_doctor': 'Médecin généraliste',
            # 'parent1': 'Parent 1',
            # 'parent2': 'Parent 2',
            'birth_date': 'Date de naissance',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form__control ',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form__control ',
                'placeholder': 'example@gmail.com'
            }),
            'gender': forms.Select(attrs={
                'class': 'form__control ',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form__control '
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form__control '
            }),
            'main_doctor': forms.Select(attrs={
                'class': 'form__control ',
            }),
            # 'parent1': forms.Select(attrs={
            #     'class': 'form__control '
            # }),
            # 'parent2': forms.Select(attrs={
            #     'class': 'form__control '
            # }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form__control ',
                'type': 'date'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].validators = []


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Ancien mot de passe',
        widget=forms.PasswordInput(attrs={
            'class': 'form__control ',
            'placeholder': 'Ancien mot de passe'
        }),
        strip=False,
        required=True
    )
    new_password1 = forms.CharField(
        label='Nouveau mot de passe',
        widget=forms.PasswordInput(attrs={
            'class': 'form__control ',
            'placeholder': 'Nouveau mot de passe'
        }),
        strip=False,
        required=True
    )
    new_password2 = forms.CharField(
        label='Confirmer le nouveau mot de passe',
        widget=forms.PasswordInput(attrs={
            'class': 'form__control ',
            'placeholder': 'Confirmer le nouveau mot de passe'
        }),
        strip=False,
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ('old_password', 'new_password1', 'new_password2')


class AddDiseaseForm(forms.Form):
    disease = forms.ModelChoiceField(
        queryset=diseases.Diseases.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form__control ',
        }),
        required=True
    )


class AddTreatmentForm(forms.Form):
    treatment = forms.ModelChoiceField(
        queryset=treatment.Treatment.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form__control ',
        }),
        required=True
    )


class AddAppointmentForm(forms.ModelForm):

    class Meta:
        model = appointment.Appointment
        fields = '__all__'

        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date'
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time'
            }),
            'doctor': forms.Select(attrs={
                'placeholder': 'Bob Dupont'
            }),
            'user': forms.Select(attrs={
                'placeholder': 'Lucie Leclerc'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Rendez-vous de routine'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': '9 rue de la source, Alençon'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form__control ',
            })


class AddPrescriptionForm(forms.ModelForm):

    class Meta:
        model = prescription.Prescription
        fields = '__all__'
        widgets = {
            'end_date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form__control ',
            })
