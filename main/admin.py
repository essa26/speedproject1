from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from main.models import SpeedModel, CustomUser
from main.forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
        fieldsets = (
                (_('User Info'), {'fields': ('email', 'password')}),
                (_('Personal info'), {'fields': ('first_name', 'last_name')}),
                (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
                (_('Important Dates'), {'fields': ('last_login', 'date_joined')}),
        )

        add_fieldsets = (
                (_('Add User'), 
                        { 
                                'classes':('wide',),
                                'fields':('email','password1','password2')
                        }
                ),
        )

        form = CustomUserChangeForm
        add_form = CustomUserCreationForm
        list_display = ('email', 'first_name', 'last_name', 'is_staff')
        search_field = ('email', 'first_name', 'last_name')
        ordering = ('email',)


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SpeedModel)