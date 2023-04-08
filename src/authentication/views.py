from django.contrib.auth.views import LoginView, LogoutView

class LoginView(LoginView):
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True

class LogoutView(LogoutView):
    template_name = None
