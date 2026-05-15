from django.contrib import admin
from .models import Thread, Reply, Profile

# Register your models here.
print("hello!")
@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish_date']
    list_filter = ['publish_date', 'author']
    search_fields = ['title', 'text']

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ['thread', 'author', 'publish_date']
    list_filter = ['publish_date', 'author']
    search_fields = ['text']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "icon"]
    search_fields = ["user_name"]
    search_help_text = ["Search by username"]