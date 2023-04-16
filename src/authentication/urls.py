from django.urls import path
from .views import LoginView, LogoutView, SignUpView, UpdateProfilePictureView

app_name = 'authentication'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('update-profile-picture/', UpdateProfilePictureView.as_view(),
         name='update_profile_picture'),
]
