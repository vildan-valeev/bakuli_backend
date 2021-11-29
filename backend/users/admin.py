from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from users.models import UserProfile, CustomUser


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profiles'


# TODO: BaseUserAdmin
class CustomUserAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline,)
    list_display = ('id', 'email', 'is_staff')
    ordering = ('id',)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name')
    ordering = ('id',)


admin.site.register(UserProfile)
admin.site.register(CustomUser, CustomUserAdmin)

admin.site.unregister(Group)
