from django import forms
from .models import Speciality
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    subject = forms.ModelMultipleChoiceField(queryset=Speciality.objects.all())
    message = forms.Textarea()


class UserCreateForm(UserCreationForm):
    email = forms.EmailField()
    full_name = forms.CharField()

    class Meta:
        model = User
        fields = ['phone', 'full_name', 'password1', 'password2']