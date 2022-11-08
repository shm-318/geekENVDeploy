from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth import get_user_model

from django.contrib.auth.admin import UserAdmin
from blog.forms import UserForm,CustomUserChangeForm
# Register your models here.

User = get_user_model()

# For Custom User Admin
class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form = CustomUserChangeForm
    model = User
    add_fieldsets = (
        ('Personal Details', {'fields': ('email', 'full_name', 'username', 'picture', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),

        )
    fieldsets = (
        ('Personal Details', {'fields': ('email', 'full_name', 'username', 'picture_url')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Optional', {'fields': ('status','website','college','country','phone_number','gender')}),
        )
# Register your models here.

admin.site.register(Contact)
admin.site.register(User,CustomUserAdmin)



