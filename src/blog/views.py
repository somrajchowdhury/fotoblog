from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import PhotoForm

class HomeView(LoginRequiredMixin, View):
    template_name = 'blog/home.html'

    def get(self, request):
        return render(request, self.template_name)

class PhotoUploadView(View):
    form_class = PhotoForm
    template_name = 'blog/photo_upload.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name,
                      context={'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('blog:home')
        return render(request, self.template_name,
                      context={'form': form})
