from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import LoginForm

class LoginView(View):
    form_class = LoginForm
    template_name = 'authentication/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name,
                      context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        message = ''

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('blog:home')
            message = 'Login failed!'

        return render(request, self.template_name,
                      context={'form': form, 'message': message})

class LogoutView(View):

    @staticmethod
    def get(self, request):
        logout(request)
        return render('authentication:login')
