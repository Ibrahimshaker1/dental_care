from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView
# Create your views here.


class SignUp(CreateView):
    success_url = ""
    template_name = "accounts/signup.html"
    form_class = forms.UserCreationForm


class DocSignup(CreateView):
    success_url = ""
    template_name = "accounts/doc_signup.html"
    form_class = forms.DoctorCreationForm

    def form_valid(self, form):
        special_condition = form.cleaned_data['special_text']
        if special_condition == 'myDoctor':
            return super().form_valid(form)
        else:
            form.add_error('special_text', 'Please provide the correct special text.')
            return self.form_invalid(form)
