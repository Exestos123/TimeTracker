from django.contrib import admin
from tracker.models import *


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(Positions)
class PositionsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(WorkCategory)
class WorkCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(TimeLine)
class SettingsAdmin(admin.ModelAdmin):
    list_display = (
        'start_at', 'end_at'
    )
