from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

class HomeView(LoginRequiredMixin, View):
    template_name = 'blog/home.html'

    def get(self, request):
        return render(request, self.template_name)
