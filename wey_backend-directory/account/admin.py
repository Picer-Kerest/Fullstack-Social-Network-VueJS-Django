from django.contrib import admin
from .models import User, FriendshipRequest
from django.urls import reverse
from django.utils.html import format_html


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'id']
    list_display_links = ('name', 'email', 'id')


# Иной способ для вставки ссылки
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('id', 'email_link', 'name')
#
#     def email_link(self, obj):
#         return format_html('<a href="{}">{}</a>', reverse('admin:%s_%s_change' % (
#             obj._meta.app_label,  obj._meta.model_name),  args=[obj.pk]), obj.email)
#     email_link.admin_order_field = 'email'
#
#     email_link.short_description = 'Email'
#
#
# admin.site.register(User, UserAdmin)


@admin.register(FriendshipRequest)
class FriendshipRequestAdmin(admin.ModelAdmin):
    list_display = ['created_by', 'created_for', 'created_at', 'status', 'id']
    list_display_links = ('created_by', 'created_for', 'created_at', 'status', 'id')

