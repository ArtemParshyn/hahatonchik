from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Employee, Project

admin.site.register(Project)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('fio', 'position', 'is_founder')
    fields = (
        'fio',
        'stazh',
        'position',
        'number',
        'mail',

        'salary',
        'age',
        'city',
        'date_of_birth',
        'is_founder',
        'zevisit',
        'project',
    )

    class Media:
        js = ('admin/employee.js',)
