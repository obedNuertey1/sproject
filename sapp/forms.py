from socket import fromshare
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import SModel


class SModelForm(forms.ModelForm):
    class Meta:
        model = SModel
        fields = ('first_name', 'last_name', 'pdf_file')
        help_texts = {
            'first_name': None,
            'last_name': None,
        }


# class SModelForm2(forms.ModelForm):
#    class Meta:
#        model = SModel
#        fields = ('student_ID', 'PIN')


# class CreateUserForm(UserCreationForm, forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ('username', 'student_ID',
#                  'PIN', 'first_name', 'last_name', 'email')

#        help_texts = {
#            'username': None,
#            'email': None,
#            'password': None,
#        }
# class CreateUserForm(UserCreationForm):
#    class Meta:
#        model = SModel
#        fields = ('first_name', 'last_name', 'student_ID',
#                  'PIN', 'password', 'password2',)

#        help_texts = {
#            'username': None,
#            'email': None,
#            'password': None,
#        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1',
                  'password2']

        help_texts = {
            'username': None,
            'email': None,
            'password': None,
        }
