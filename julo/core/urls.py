from django.urls import path,include
from core import views
from django.conf.urls import url

app_name = 'core'

urlpatterns = [
    path('signup/',views.user_signup, name="signup"),
]
