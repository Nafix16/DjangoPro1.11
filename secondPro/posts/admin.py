from django.contrib import admin
from django.db import models
from .models import Post, Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class PostModelAdmin(admin.ModelAdmin):

    list_display = ["title", "updated", "timestamp", "image"]
    list_display_links = ["updated", "title"]
    search_fields = ["title", "contents"]
    add_form_template = "base.html"

    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
admin.site.register(Profile)

