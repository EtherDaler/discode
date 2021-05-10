from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import UserCreationForm, UserChangeForm
from .models import *

class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['phone', 'email', 'subscribe', 'admin', 'staff', 'partner', 'client']
    list_filter = ['date_of_register', 'last_visit', 'subscribe', 'admin', 'staff', 'partner', 'client']
    """
    fieldsets = (
        (None, {'fields': ('phone', 'email','password')}),
        ('Permissions', {'fields': ('admin', 'staff', 'is_active')}),
    )
    """
    fieldsets = (
        (None, {'fields': ('phone', 'email','password')}),
        ('Personal info', {'fields': ('first_name', 'subscribe', 'partner', 'client', 'date_of_register', 'last_visit', 'login_count')}),
        ('Permissions', {'fields': ('admin', 'staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'email', 'first_name', 'subscribe', 'partner', 'client', 'password1', 'password2')}
        ),
    )
    search_fields = ('phone', 'email', 'first_name')
    ordering = ('phone', 'email')

admin.site.register(User, UserAdmin)

admin.site.unregister(Group)