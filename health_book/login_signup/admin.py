from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from login_signup.models import appointment, customUser, diseases, doctor, job, location, rpps, treatment, trustedUser, userDisease
# from login_signup.models import *


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


class CustomAppointmentAdmin(admin.StackedInline):
    model = appointment.Appointment
    # Limit the number of appointments to 1
    max_num = 1


class CustomLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'postal_code')
    inlines = [CustomAppointmentAdmin]


# Register your models here.
admin.site.register(diseases.Diseases)
admin.site.register(rpps.RPPS, CustomRPPSAdmin)
admin.site.register(job.Job)
admin.site.register(location.Location, CustomLocationAdmin)
admin.site.register(doctor.Doctor, CustomDoctorAdmin)
admin.site.register(customUser.CustomUser, CustomUserAdmin)
admin.site.register(treatment.Treatment)
admin.site.register(trustedUser.TrustedPerson)
admin.site.register(userDisease.UserDisease)
admin.site.register(appointment.Appointment)
