from django import forms

from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Enter email'
    }), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control",
        'placeholder': 'Enter password'
    }), required=True)

    def clean_email(self):
        form_data = self.cleaned_data
        user = User.objects.filter(email=form_data['email'])
        if not user.exists():
            raise forms.ValidationError('User does not exists')
        return form_data['email']


class RegisterForm(LoginForm):
    confirm_password = forms.CharField(label='Confirm Password', max_length=100,
                                       widget=forms.PasswordInput(attrs={
                                           'class': "form-control",
                                           'placeholder': 'Confirm password'
                                       }), required=True)

    def clean_email(self):
        form_data = self.cleaned_data
        user = User.objects.filter(email=form_data['email'])
        if user.exists():
            raise forms.ValidationError('User already exists')
        return form_data['email']

    def clean_confirm_password(self):
        form_data = self.cleaned_data
        if form_data['password'] != form_data['confirm_password']:
            raise forms.ValidationError('Password do not match')
        return form_data['confirm_password']
