from re import A
from django.contrib import admin
# Register your models here.
from .models import UserProfile


from django.contrib.auth.admin import UserAdmin
from .models import User, Supplier, Project, QuoteHeader, QuoteBody, Item, ItemCategory, ItemView ,ItemUnit

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
admin.site.register(Supplier)
admin.site.register(Project)
admin.site.register(QuoteHeader)
admin.site.register(QuoteBody)
admin.site.register(Item)
admin.site.register(ItemCategory)
admin.site.register(ItemView)
admin.site.register(ItemUnit)
