from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models


class UserCreationForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        # it is like what will show in the label or what the type of the label
        self.fields['username'].label = "Display Name"
        self.fields['email'].label = "Email Address"


class DoctorCreationForm(UserCreationForm):

    special_text = forms.CharField(max_length=100)
    Phone_number = forms.CharField(max_length=20)
    graduate_year = forms.CharField(max_length=10)
    dental_doctor = forms.BooleanField()

    class Meta:
        fields = ('username', 'email', 'Phone_number', 'graduate_year', 'dental_doctor', 'password1', 'password2', 'special_text')
        model = get_user_model()

    def __init__(self, *args, **Kwargs):
        super().__init__(*args, **Kwargs)
        # it is like what will show in the label or what the type of the label
        self.fields['username'].label = "Display Name"
        self.fields['email'].label = "Email Address"


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = models.Appointment
        fields = ['first_name', 'list_name', 'phone_number', 'datetime_field']

