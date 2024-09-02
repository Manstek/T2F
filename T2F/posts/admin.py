from django.contrib import admin
from . models import Post, Group, Comment, Like
# Register your models here.

admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Comment)
admin.site.register(Like)
