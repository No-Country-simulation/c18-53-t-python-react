from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from .models import User

# Register your models here.

class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display =['email', 'first_name', 'last_name', 'user_type']
    readonly_fields = ['date_joined', 'last_login']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('User Type'), {'fields': ('user_type',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'user_type', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )



admin.site.register(User, UserAdmin)
