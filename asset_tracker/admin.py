"""Django admin customization"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _


from asset_tracker.models import (
    User,
    Company,
    Employee,
    Device,
    DeviceAssignment
)


class UserAdmin(BaseUserAdmin):
    """Define the admin page for user"""

    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email','password')}),
        (
            _('permission'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (
            _('Important dates'),
            {
                'fields': (
                    'last_login',
                )
            }
        ),

    )

    readonly_fields = ['id']

    add_fieldsets = (
        (None,
         {
             'classes': ('wide',),
             'fields': (
                 'email',
                 'password1',
                 'password2',
                 'name',
                 'is_active',
                 'is_staff',
                 'is_superuser',
             )
         }
         ),
    )


admin.site.register(User, UserAdmin)
admin.site.site_header = "Asset Tracker API"
admin.site.site_title = "Corporate Asset Tracker Django REST API"
admin.site.index_title = "Welcome Admin"


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'phone_number')
    search_fields = ('name',)


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'condition', 'company', 'checked_out')
    search_fields = ('name', 'serial_number')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ('company', 'devices')


@admin.register(DeviceAssignment)
class DeviceAssignmentAdmin(admin.ModelAdmin):
    list_display = ('device', 'employee', 'assigned_date', 'return_date', 'updated_at')
    search_fields = ('device', 'employee__name')