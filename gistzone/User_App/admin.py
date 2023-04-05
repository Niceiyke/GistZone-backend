from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import myUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = myUser
    list_display = ('email', 'is_staff', 'is_active','is_veryfied','is_banned','is_suspended',)
    list_filter = ('email', 'is_staff', 'is_active','is_veryfied','is_banned','is_suspended',)
    fieldsets = (
        (None, {'fields': ('email','username','first_name','last_name','rank','password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_veryfied','is_banned','is_suspended',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','username','first_name','last_name','password1', 'password2', 'is_staff', 'is_active''is_veryfied','is_banned','is_suspended',)}
        ),
    )
    search_fields = ('email','username','first_name','last_name','rank',)
    ordering = ('email',)


admin.site.register(myUser, CustomUserAdmin)
