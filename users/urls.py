from django.urls import path
from .views import Candidate, Userprofile, LoginView, SignUpView, PasswordChangeView
# from django.views.generic import TemplateView

urlpatterns = [
    # path('sign/', SignUpView.as_view(), name='sign'),
    # path('login/', LogInView.as_view(), name='login'),
    # path('register_user/', register_user, name='register'),
    path('candidate/', Candidate.as_view(), name='candidate'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', SignUpView.as_view(), name='register'),
    path('password_change/', PasswordChangeView.as_view(), name='password-change'),

    # profile
    path('profile/my-courses/', Userprofile.as_view(), name='profile-courses'),
    path('profile/all-courses/', Userprofile.as_view(), name='profile-all-courses'),
    path('profile/certificate/', Userprofile.as_view(), name='profile-certificate'),
    path('profile/payment/', Userprofile.as_view(), name='profile-payment'),
    path('profile/devices/', Userprofile.as_view(), name='profile-devices'),
    path('profile/events/', Userprofile.as_view(), name='profile-events'),
    path('profile/settings/', Userprofile.as_view(), name='profile-settings'),
]