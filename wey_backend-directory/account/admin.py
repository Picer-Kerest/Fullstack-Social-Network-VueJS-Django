from django.contrib import admin
from .models import User, FriendshipRequest


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'name']


@admin.register(FriendshipRequest)
class FriendshipRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_by', 'created_for', 'created_at', 'status']

