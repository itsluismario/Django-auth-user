from django.urls import path
from core import views


app_name = 'core'

urlpatterns = [
    path('index',views.index, name="index"),
    path('',views.user_login, name="login"),
    path('signup/',views.user_signup, name="signup"),
    path('email_verification/',views.email_verification, name="emailVerification"),
]
