from django.contrib import admin
from .models import Todo

# Register your models here.

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_completed','create_at')
    list_filter = ('is_completed',)
    search_fields = ('title','description')


