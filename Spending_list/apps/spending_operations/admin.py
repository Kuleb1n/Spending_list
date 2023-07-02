from django.contrib import admin

from .models import Operation, Goal


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'cost', 'operation_at')
    list_display_links = ('name',)
    list_filter = ('operation_at',)
    search_fields = ('name',)
    ordering = ('-operation_at',)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'goal_type', 'start_date', 'finish_date', 'value',)
    list_display_links = ('name',)
    search_fields = ('name',)
