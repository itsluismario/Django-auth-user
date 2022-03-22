from django.contrib import admin
# Register your models here.
from .models import UserProfile


from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
