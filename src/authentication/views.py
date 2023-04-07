from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def login_view(request):
    form = LoginForm()
    message = ''

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                message = f'Hello {user.username}! Welcome back.'
            else:
                message = 'Login failed!'

    context = {'form': form, 'message': message}

    return render(request,
                  template_name='authentication/login.html',
                  context=context)

def logout_view(request):
    logout(request)
    return redirect('authentication:login')
