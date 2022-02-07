from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from login_signup.models import *


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'gender',
                    'parent1',
                    'parent2',
                    'main_doctor',
                    'birth_date',
                    'treatments'
                ),
            },
        ),
    )


class CustomDoctorAdmin(admin.ModelAdmin):
    list_display = ('rpps', 'job')


class CustomRPPSAdmin(admin.ModelAdmin):
    list_display = ('rpps', 'firstname', 'lastname')


class CustomLocationAdmin(admin.ModelAdmin):
    list_display = ('user',)


# Register your models here.
admin.site.register(Diseases)
admin.site.register(RPPS, CustomRPPSAdmin)
admin.site.register(Job)
admin.site.register(Location, CustomLocationAdmin)
admin.site.register(Doctor, CustomDoctorAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Treatment)
admin.site.register(TrustedPerson)
admin.site.register(UserDisease)
