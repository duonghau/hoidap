from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

# Register your models here.
class UserProfileInline(admin.StackedInline): 
    model = UserProfile 

class UserProfileAdmin(UserAdmin): 
    inlines = [UserProfileInline] 
    
admin.site.unregister(User) 
admin.site.register(User, UserProfileAdmin)