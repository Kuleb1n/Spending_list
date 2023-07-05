from django.contrib import admin

from .models import Operation, Goal, Category


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'category', 'cost', 'operation_at')
    list_display_links = ('name', 'category')
    list_filter = ('operation_at', 'category')
    search_fields = ('name',)
    ordering = ('-operation_at',)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'goal_type', 'start_date', 'finish_date', 'value',)
    list_display_links = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)
    search_fields = ('name',)
