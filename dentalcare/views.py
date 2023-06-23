from django.views.generic import TemplateView


class Homepage(TemplateView):

    template_name = "index.html"


class SignupPage(TemplateView):

    template_name = "signup_page.html"
