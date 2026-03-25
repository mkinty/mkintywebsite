from django.contrib import admin

from apps.users.models import User


# Register your models here.
@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('first_name', 'last_name',)
    search_fields = ('email',)
