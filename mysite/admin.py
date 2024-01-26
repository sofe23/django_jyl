from django.contrib import admin
from .models import MainContent, Comment

class MainContentAdmin(admin.ModelAdmin):
    list_display = ['title','content','pub_date', 'main_image']
    search_fields = ['title']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author']

admin.site.register(MainContent, MainContentAdmin)
admin.site.register(Comment, CommentAdmin)
# Register your models here.
