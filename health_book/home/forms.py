from django import forms
from login_signup.models import CustomUser, Doctor


class UserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username',
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
