from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'address', 'date_of_birth',
                  'experience', 'position', 'education', 'company', 'linkedin', "year"]
