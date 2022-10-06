from re import A
from django.contrib import admin
# Register your models here.
from .models import UserProfile


from django.contrib.auth.admin import UserAdmin
from .models import User, Supplier, Project, Quote, Material

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
admin.site.register(Supplier)
admin.site.register(Project)
admin.site.register(Quote)
admin.site.register(Material)