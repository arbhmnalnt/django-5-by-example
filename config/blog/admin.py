from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display    =    ('title', 'slug', 'created')
    search_fields   =   ('title', 'body')
    prepopulated_fields =   {'slug':('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display    =   ('name', 'post', 'created', 'active')
    search_fields   =   ('name', 'body')
    list_filter     =   ('active', 'created')
    actions         =   ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.upda
