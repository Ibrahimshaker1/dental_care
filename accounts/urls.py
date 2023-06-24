from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="Signup"),
    path("doctor signup/", views.DocSignup.as_view(), name="doc_signup"),
    path("Login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="Login"),
    path("Logout/", auth_views.LogoutView.as_view(), name="Logout"),
    path("appointment/", views.AppointmentView.as_view(), name="appointment")
]

