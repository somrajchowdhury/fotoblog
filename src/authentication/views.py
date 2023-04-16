from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model
from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import SignUpForm, UpdateProfilePictureForm

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

class UpdateProfilePictureView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = UpdateProfilePictureForm
    template_name = 'authentication/update_profile_picture.html'
    success_url = reverse_lazy('blog:home')

    def get_object(self, queryset=None):
        return self.request.user
