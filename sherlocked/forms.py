from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):

    username = forms.CharField()
    your_name = forms.CharField(label='Your name', max_length=100)
    #password = forms.CharField(widgets=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField(label='Email Id')
    zeal_Id=forms.CharField()
    Year=forms.DecimalField(min_value=1,max_value=4)
    class Meta:
        model = User
        fields = ('username','email')

#class RegistrationForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput)
