from email.mime import message
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from login_signup.models import appointment, customUser, diseases, doctor, job, location, rpps, treatment, trustedUser, userDisease
from login_signup.models import *


class CustomDiseasesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', '__str__')


class CustomUserDiseasesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', '__str__')


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'Extra field',  # heading
            {
                'fields': (
                    'gender',
                    'parent1',
                    'parent2',
                    'main_doctor',
                    'birth_date',
                    'treatments',
                    'blocked_user',
                ),
            },
        ),
    )
    list_display = ('id', '__str__', 'role')


class CustomDoctorAdmin(admin.ModelAdmin):
    list_display = ('rpps', 'job')


class CustomRPPSAdmin(admin.ModelAdmin):
    list_display = ('rpps', 'firstname', 'lastname')


class CustomLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'postal_code')


class CustomPrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'doctor', 'treatment')


# Register your models here.
admin.site.register(diseases.Diseases, CustomDiseasesAdmin)
admin.site.register(rpps.RPPS, CustomRPPSAdmin)
admin.site.register(job.Job)
admin.site.register(location.Location, CustomLocationAdmin)
admin.site.register(doctor.Doctor, CustomDoctorAdmin)
admin.site.register(customUser.CustomUser, CustomUserAdmin)
admin.site.register(treatment.Treatment)
admin.site.register(trustedUser.TrustedPerson)
admin.site.register(userDisease.UserDisease, CustomUserDiseasesAdmin)
admin.site.register(appointment.Appointment)
admin.site.register(prescription.Prescription, CustomPrescriptionAdmin)
admin.site.register(message.Message)
admin.site.register(notification.Notification)
