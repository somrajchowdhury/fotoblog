from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.views.generic.list import ListView
from .forms import PhotoForm, BlogForm
from .models import Photo, Blog

class HomeView(LoginRequiredMixin, ListView):
    model = Photo
    context_object_name = 'photos'
    template_name = 'blog/home.html'

class PhotoUploadView(LoginRequiredMixin, View):
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

class CreateBlogPostView(LoginRequiredMixin, View):
    photo_form = PhotoForm
    blog_form = BlogForm
    template_name = 'blog/create_blog_post.html'

    def get(self, request):
        photo_form = self.photo_form()
        blog_form = self.blog_form()
        return render(request, self.template_name,
                      context={'photo_form': photo_form,
                               'blog_form': blog_form})

    def post(self, request):
        photo_form = self.photo_form(request.POST, request.FILES)
        blog_form = self.blog_form(request.POST)
        if all([photo_form.is_valid(), blog_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog_post = blog_form.save(commit=False)
            blog_post.photo = photo
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog:home')
        return render(request, self.template_name,
                      context={'photo_form': photo_form,
                               'blog_form': blog_form})

class BlogPostListView(LoginRequiredMixin, ListView):
    model = Blog
    context_object_name = 'blog_posts'
    template_name = 'blog/blog_post_list.html'
