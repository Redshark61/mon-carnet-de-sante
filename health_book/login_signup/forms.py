from django import forms
from login_signup.models import CustomUser, Location


class Connection1(forms.Form):

    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form__control btn btn--dark-green',
                                     'placeholder': 'First Name'
                                 }))
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={
                                    'class': 'form__control btn btn--dark-green',
                                    'placeholder': 'First Name'
                                }))
    mail = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form__control btn btn--dark-green',
        'placeholder': 'exemple@gmail.com'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form__control btn btn--dark-green',
        'autocomplete': 'false',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form__control btn btn--dark-green',
        'autocomplete': 'false',
    }))


class Connection2(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['gender', 'birth_date']
        widgets = {
            'gender': forms.Select(attrs={
                'class': 'form__control btn btn--dark-green'
            }),
            'birth_date': forms.DateInput(attrs={'class': 'form__control btn btn--dark-green', 'type': 'date'})
        }


class Connection3(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['city', 'address']
        widgets = {
            'city': forms.TextInput(attrs={
                'class': 'form__control js-input-cities',
                'placeholder': '61250',
                'list': 'city--list'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form__control btn btn--dark-green js-input-address',
                'placeholder': '12 bis rue des sources'
            })
        }


class Connection4(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['city', 'address']
        widgets = {
            'city': forms.TextInput(attrs={
                'class': 'form__control js-input-cities',
                'placeholder': '61250',
                'list': 'city--list'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form__control btn btn--dark-green js-input-address',
                'placeholder': '12 bis rue des sources'
            })
        }


class LoginForm(forms.Form):

    id_code = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form__control btn btn--dark-green js-security-code',
               'placeholder': '0-00-00-00-000-000 0'}))

    rpps_code = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form__control btn btn--dark-green',
               'placeholder': '0123456789012'}))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form__control btn btn--dark-green',
               'autocomplete': 'false',
               'placeholder': 'password'}))
