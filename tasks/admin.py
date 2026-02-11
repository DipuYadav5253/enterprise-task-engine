from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # This makes the admin panel look professional by showing columns
    list_display = ('title', 'owner', 'priority', 'is_completed', 'created_at')
    list_filter = ('priority', 'is_completed', 'owner')
    search_fields = ('title', 'description')