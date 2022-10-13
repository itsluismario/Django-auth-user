from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import UserPasswordResetForm


app_name = 'users'

urlpatterns = [
    path('index',views.index, name="index"),
    path('',views.user_login, name="login"),
    path('signup/',views.user_signup, name="signup"),
    path('email_verification/',views.email_verification, name="emailVerification"),
   
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html',
         form_class=UserPasswordResetForm),
         name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete')
    
]
