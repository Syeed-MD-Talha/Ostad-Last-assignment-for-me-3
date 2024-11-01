from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Ensure super() directly calls AuthenticationForm's __init__
        self.fields['username'].widget.attrs.update({'class': 'form-control','id': 'fullName', 'placeholder': 'Username','required': True})
        self.fields['password'].widget.attrs.update({'class': 'form-control','id': 'password', 'placeholder': 'Password','required': True})
        
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(max_length=65)
#     password = forms.CharField(max_length=65, widget=forms.PasswordInput)
#     def __init__(self, *args, **kwargs):
#         super(RegisterForm, self).__init__(*args, **kwargs)
#         self.fields['username'].widget = forms.TextInput(attrs={
#             'class': 'form-control',
#             'id': 'fullName',
#             'required': True
#         })
#         self.fields['password'].widget = forms.PasswordInput(attrs={
#             'class': 'form-control',
#             'id': 'password',
#             'required': True
#         })


    
    
    
    

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'fullName',
            'required': True
        })
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'id': 'email',
            'required': True
        })
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'password',
            'required': True
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'confirmPassword',
            'required': True
        })
