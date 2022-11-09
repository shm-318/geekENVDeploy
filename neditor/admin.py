from django.contrib import admin

# Register your models here.

from django.contrib import admin
from neditor.models import Post, Comment, Follow


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ('content',)


""" @admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
 """


class PostModelAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('id','user','created_on')
    inlines = [
        CommentInline,
    ]


admin.site.register(Post,PostModelAdmin)
admin.site.register(Follow)
admin.site.register(Comment)