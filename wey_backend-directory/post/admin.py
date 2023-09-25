from django.contrib import admin
from .models import Post, PostAttachment, Comment, Like

admin.site.register(Post)
admin.site.register(PostAttachment)
# admin.site.register(Comment)
admin.site.register(Like)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['created_by', 'id', 'slices']
    list_display_links = ('created_by', 'id', 'slices')

    def slices(self, obj):
        return obj.body[:150]


