from datetime import datetime
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "home/register_user.html"
    success_url = "/notes"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("notes.list")
        return super().get(request, *args, **kwargs)

class LogoutInterfaceView(LogoutView):
    template_name = "home/logout_page.html"

class LoginInterfaceView(LoginView):
    template_name = "home/login_page.html"

class HomeView(TemplateView):
    template_name = "home/welcome.html"
    extra_context = {'today':datetime.today()}

class AuthView(LoginRequiredMixin, TemplateView):
    template_name = "home/auth.html"
    login_url='admin'

