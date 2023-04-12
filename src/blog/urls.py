from django.urls import path
from .views import HomeView, PhotoUploadView

app_name = 'blog'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('upload-photo/', PhotoUploadView.as_view(), name='photo_upload'),
]
