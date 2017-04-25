"""Result Task Admin interface."""
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from .models import TaskResult


class TaskResultAdmin(admin.ModelAdmin):
    """Admin-interface for results of tasks."""

    model = TaskResult
    list_display = (
        'task_id', 'date_done', 'task_name', 'status', 'task_arguments')
    list_filter = ('task_name', 'status')
    readonly_fields = (
        'date_done', 'result', 'hidden', 'meta', 'task_arguments', 'task_name')
    fieldsets = (
        (None, {
            'fields': (
                'task_id',
                'task_name',
                'status',
                'content_type',
                'task_arguments',
                'content_encoding',
            ),
            'classes': ('extrapretty', 'wide')
        }),
        ('Result', {
            'fields': (
                'result',
                'date_done',
                'traceback',
                'hidden',
                'meta',
            ),
            'classes': ('extrapretty', 'wide')
        }),
    )


admin.site.register(TaskResult, TaskResultAdmin)
