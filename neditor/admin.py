from django.contrib import admin

# Register your models here.

from django.contrib import admin
from neditor.models import Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ('content',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
