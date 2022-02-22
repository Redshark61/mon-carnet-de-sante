from django.urls import path
from .views.appointmentsView import AppointmentsView
from .views.deleteView import DeleteView
from .views.diseaseView import DiseasesView
from .views.homeView import HomeView
from .views.passwordSuccess import passwordSuccess
from .views.settingsView import SettingsView
from .views.treatmentView import TreatmentsView
from .views.editTreatment import EditTreatment
from .views.changePasswordView import ChangePasswordView
from .views.addDisease import AddDisease
from .views.editDisease import EditDisease
from .views.deleteDisease import DeleteDisease
from .views.addTreatment import AddTreatment
from .views.deleteTreatment import DeleteTreatment
from .views.addAppointment import AddAppointment
from .views.prescriptionView import PrescriptionView
from .views.addPrescriptionView import AddPrescriptionView
from .views.patientsView import PatientsView
from .views.patientView import PatientView
from .views.patientDiseasesView import PatientDiseasesView
from .views.patientTreatmentsView import PatientTreatmentsView
from .views.deleteAppointementView import DeleteAppointementView
from .views.editAppointementView import EditAppointementView
from .views.restoreAppointment import RestoreAppointementView
from .views.detailPrescriptionView import DetailPrescriptionView

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    ### Disease ###
    path('diseases/', DiseasesView.as_view(), name="diseases"),
    path('disease/add', AddDisease.as_view(), name="add_disease"),
    path('disease/delete/<int:pk>', DeleteDisease.as_view(), name="delete_disease"),
    path('disease/edit/<int:pk>', EditDisease.as_view(), name="edit_disease"),
    ### Treatment ###
    path('treatments/', TreatmentsView.as_view(), name="treatments"),
    path('treatment/add', AddTreatment.as_view(), name="add_treatment"),
    path('treatment/edit/<int:pk>', EditTreatment.as_view(), name="edit_treatment"),
    path('treatment/delete/<int:pk>', DeleteTreatment.as_view(), name="delete_treatment"),
    ### Appointment ###
    path('appointments/', AppointmentsView.as_view(), name="appointments"),
    path('appointement/delete/<int:pk>', DeleteAppointementView.as_view(), name="delete_appointement"),
    path('appointments/edit/<int:pk>', EditAppointementView.as_view(), name="edit_appointement"),
    path('appointment/add', AddAppointment.as_view(), name="add_appointment"),
    path('appointment/restore/<int:pk>', RestoreAppointementView.as_view(), name="restore_appointment"),
    ### Prescription ###
    path('prescription/', PrescriptionView.as_view(), name="prescription"),
    path('prescription/add', AddPrescriptionView.as_view(), name="prescription_add"),
    path('prescription/detail/<int:pk>', DetailPrescriptionView.as_view(), name="prescription_detail"),
    ### Patients ###
    path('patients', PatientsView.as_view(), name="patients_view"),
    path('patient/<int:pk>', PatientView.as_view(), name="patient_view"),
    path('patient/<int:pk>/diseases', PatientDiseasesView.as_view(), name="patient_diseases_view"),
    path('patient/<int:pk>/treatments', PatientTreatmentsView.as_view(), name="patient_treatments_view"),
    ### Settings ###
    path('settings/', SettingsView.as_view(), name="settings"),
    path('settings/delete', DeleteView.as_view(), name="delete"),
    path('settings/password', ChangePasswordView.as_view(), name="password_change"),
    path('settings/password_success', passwordSuccess, name="password_success"),
]
