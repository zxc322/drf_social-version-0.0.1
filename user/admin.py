from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


class ExtendedUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'phone', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Info'), {'fields': ('phone', 'avatar', 'gender', 'interests_tags', 'own_interests')}),
    )


admin.site.register(ExtendedUser, ExtendedUserAdmin)


@admin.register(InterestsTags)
class InterestsTagsAdmin(admin.ModelAdmin):
    pass


@admin.register(OwnInterests)
class OwnInterestsAdmin(admin.ModelAdmin):
    pass