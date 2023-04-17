from django.urls import path
from .views import HomeView, PhotoUploadView, CreateBlogPostView

app_name = 'blog'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('upload-photo/', PhotoUploadView.as_view(), name='photo_upload'),
    path('create-blog/', CreateBlogPostView.as_view(), name='create_blog')
]
