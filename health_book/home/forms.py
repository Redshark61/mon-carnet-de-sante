from django import forms
from login_signup.models import CustomUser


class UserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username',
                  'email',
                  'password',
                  'gender',
                  'first_name',
                  'last_name',
                  'main_doctor',
                  'parent1',
                  'parent2',
                  'birth_date',
                  )
        labels = {
            'username': 'Nom d\'utilisateur',
            'email': 'Adresse email',
            'password': 'Mot de passe',
            'gender': 'Sexe',
            'first_name': 'Prénom',
            'last_name': 'Nom de famille',
            'main_doctor': 'Médecin généraliste',
            'parent1': 'Parent 1',
            'parent2': 'Parent 2',
            'birth_date': 'Date de naissance',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form__control btn',
                'placeholder': 'Username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form__control btn',
                'placeholder': 'example@gmail.com'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form__control btn',
                'placeholder': 'Password'
            }),
            'gender': forms.Select(attrs={
                'class': 'form__control btn',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form__control btn'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form__control btn'
            }),
            'main_doctor': forms.Select(attrs={
                'class': 'form__control btn',
            }),
            'parent1': forms.Select(attrs={
                'class': 'form__control btn'
            }),
            'parent2': forms.Select(attrs={
                'class': 'form__control btn'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form__control btn',
                'type': 'date'
            })
        }
