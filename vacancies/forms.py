from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from vacancies.models import Application, Company, Vacancy, Specialty, Resume


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='Имя')
    last_name = forms.CharField(max_length=30, label='Фамилия')

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'password1', 'password2',)

