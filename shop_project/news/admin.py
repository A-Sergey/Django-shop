from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','publish')
    list_filter = ('title','publish')
    search_fields = ('title','body')
    ordering = ['publish']

admin.site.register(Post, PostAdmin)

