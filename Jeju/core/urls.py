from django.urls import path

from django.contrib.auth import views as auth_views

from . import views


app_name = 'core'

urlpatterns = [
    path('index',views.index, name="index"),
    path('',views.user_login, name="login"),
    path('signup/',views.user_signup, name="signup"),
    path('email_verification/',views.email_verification, name="emailVerification"),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_v3.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="reset_password_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="reset_password_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="reset_password_complete"),
    
]
