from django.urls import path
from home.views.disease import addDisease, deleteDisease, diseaseView, editDisease
from django.contrib.auth.decorators import login_required
from home.views.appointment import addAppointment, deleteAppointementView, appointmentsView, editAppointementView, restoreAppointment
from home.views.treatment import addTreatment, deleteTreatment, treatmentView, editTreatment
from home.views.prescription import addPrescriptionView, deletePrescriptionView, prescriptionView, detailPrescriptionView, editPrescriptionView, restorePrescriptionView
from home.views.patient import patientsView, patientView, patientDiseasesView, patientTreatmentsView
from .views.deleteView import DeleteView
from .views.homeView import HomeView
from .views.passwordSuccess import passwordSuccess
from .views.settingsView import SettingsView
from .views.changePasswordView import ChangePasswordView
from .views.messagesView import MessagesView
from .views.messageView import MessageView

app_name = 'home'
urlpatterns = [
    path('', login_required(HomeView.as_view(), redirect_field_name=None), name="home"),
    path('message/', login_required(MessagesView.as_view(), redirect_field_name=None), name="messages"),
    path('message/<str:slug>', login_required(MessageView.as_view(), redirect_field_name=None), name="message"),
    ### Disease ###
    path('diseases/', login_required(diseaseView.DiseasesView.as_view(), redirect_field_name=None), name="diseases"),
    path('disease/add', login_required(addDisease.AddDisease.as_view(),
         redirect_field_name=None), name="add_disease"),
    path('disease/delete/<int:pk>', login_required(deleteDisease.DeleteDisease.as_view(),
         redirect_field_name=None), name="delete_disease"),
    path('disease/edit/<int:pk>', login_required(editDisease.EditDisease.as_view(),
         redirect_field_name=None), name="edit_disease"),
    ### Treatment ###
    path('treatments/', login_required(treatmentView.TreatmentsView.as_view(),
         redirect_field_name=None), name="treatments"),
    path('treatment/add', login_required(addTreatment.AddTreatment.as_view(),
         redirect_field_name=None), name="add_treatment"),
    path('treatment/edit/<int:pk>', login_required(editTreatment.EditTreatment.as_view(),
         redirect_field_name=None), name="edit_treatment"),
    path('treatment/delete/<int:pk>', login_required(deleteTreatment.DeleteTreatment.as_view(),
         redirect_field_name=None), name="delete_treatment"),
    ### Appointment ###
    path('appointments/', login_required(appointmentsView.AppointmentsView.as_view(),
         redirect_field_name=None), name="appointments"),
    path('appointement/delete/<int:pk>',
         login_required(deleteAppointementView.DeleteAppointementView.as_view(), redirect_field_name=None), name="delete_appointement"),
    path('appointments/edit/<int:pk>', login_required(editAppointementView.EditAppointementView.as_view(),
         redirect_field_name=None), name="edit_appointement"),
    path('appointment/add', login_required(addAppointment.AddAppointment.as_view(),
         redirect_field_name=None), name="add_appointment"),
    path('appointment/restore/<int:pk>',
         login_required(restoreAppointment.RestoreAppointementView.as_view(), redirect_field_name=None), name="restore_appointment"),
    ### Prescription ###
    path('prescription/', login_required(prescriptionView.PrescriptionView.as_view(),
         redirect_field_name=None), name="prescription"),
    path('prescription/add', login_required(addPrescriptionView.AddPrescriptionView.as_view(),
         redirect_field_name=None), name="prescription_add"),
    path('prescription/detail/<int:pk>',
         login_required(detailPrescriptionView.DetailPrescriptionView.as_view(), redirect_field_name=None), name="prescription_detail"),
    path('prescription/delete/<int:pk>',
         login_required(deletePrescriptionView.DeletePrescriptionView.as_view(), redirect_field_name=None), name="prescription_delete"),
    path('prescription/edit/<int:pk>',
         login_required(editPrescriptionView.EditPrescriptionView.as_view(), redirect_field_name=None), name="prescription_edit"),
    path('prescription/restore/<int:pk>',
         login_required(restorePrescriptionView.RestorePrescriptionView.as_view(), redirect_field_name=None), name="prescription_restore"),
    ### Patients ###
    path('patients', login_required(patientsView.PatientsView.as_view(),
         redirect_field_name=None), name="patients_view"),
    path('patient/<int:pk>', login_required(patientView.PatientView.as_view(),
         redirect_field_name=None), name="patient_view"),
    path('patient/<int:pk>/diseases', login_required(patientDiseasesView.PatientDiseasesView.as_view(),
         redirect_field_name=None), name="patient_diseases_view"),
    path('patient/<int:pk>/treatments', login_required(patientTreatmentsView.PatientTreatmentsView.as_view(), redirect_field_name=None),
         name="patient_treatments_view"),
    ### Settings ###
    path('settings/', login_required(SettingsView.as_view(), redirect_field_name=None), name="settings"),
    path('settings/delete', login_required(DeleteView.as_view(), redirect_field_name=None), name="delete"),
    path('settings/password', login_required(ChangePasswordView.as_view(),
         redirect_field_name=None), name="password_change"),
    path('settings/password_success', login_required(passwordSuccess,
         redirect_field_name=None), name="password_success"),
]
