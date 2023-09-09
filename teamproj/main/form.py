from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile,Films
from django.forms.models import ModelForm

from django.forms.widgets import FileInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
         'img': FileInput(),
         }


class FilmsForm(ModelForm):
    class Meta:
        model = Films
        fields = ['title', 'description','image','genres']


