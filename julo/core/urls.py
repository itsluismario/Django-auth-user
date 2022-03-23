from django.urls import path,include
from core import views
from django.conf.urls import url

app_name = 'core'

urlpatterns = [
    path('',views.user_login, name="login"),
    path('signup/',views.user_signup, name="signup"),
    path('email_verification/',views.email_verification, name="emailVerification"),
]
