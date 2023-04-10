from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import View
from django.shortcuts import render, redirect
from .forms import SignUpForm

class LoginView(LoginView):
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True

class LogoutView(LogoutView):
    template_name = None

class SignUpView(View):
    form_class = SignUpForm
    template_name = 'authentication/signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name,
                      context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('authentication:login')
        return render(request, self.template_name,
                      context={'form': form})
