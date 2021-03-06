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
from .views.customProfilePicture import CustomProfilePicture
from .views.message import messageView, messagesView, blockUser
from .views.chart import ChartView
from .views.chartYear import ChartYearView
from .views.news import newsListView, addNews, deleteNews


app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('charts', ChartView.as_view(), name="chart_view"),
    path('charts/year', ChartYearView.as_view(), name="chart_year_view"),
    ### News ###
    path('news/', newsListView.NewsListView.as_view(), name="newsList"),
    path('news/add/', addNews.AddNews.as_view(), name="addNews"),
    path('news/delete/<int:pk>', deleteNews.DeleteNews.as_view(), name="deleteNews"),
    ### Message ###
    path('message/', messagesView.MessagesView.as_view(), name="messages"),
    path('message/block/<str:slug>', blockUser.BlockUser.as_view(), name="block"),
    path('message/<str:slug>', messageView.MessageView.as_view(), name="message"),
    ### Disease ###
    path('diseases/', diseaseView.DiseasesView.as_view(), name="diseases"),
    path('disease/add', addDisease.AddDisease.as_view(), name="add_disease"),
    path('disease/delete/<int:pk>', deleteDisease.DeleteDisease.as_view(), name="delete_disease"),
    path('disease/edit/<int:pk>', editDisease.EditDisease.as_view(), name="edit_disease"),
    ### Treatment ###
    path('treatments/', treatmentView.TreatmentsView.as_view(), name="treatments"),
    path('treatment/add', addTreatment.AddTreatment.as_view(), name="add_treatment"),
    path('treatment/edit/<int:pk>', editTreatment.EditTreatment.as_view(), name="edit_treatment"),
    path('treatment/delete/<int:pk>', deleteTreatment.DeleteTreatment.as_view(), name="delete_treatment"),
    ### Appointment ###
    path('appointments/', appointmentsView.AppointmentsView.as_view(), name="appointments"),
    path('appointement/delete/<int:pk>',
         deleteAppointementView.DeleteAppointementView.as_view(), name="delete_appointement"),
    path('appointments/edit/<int:pk>', editAppointementView.EditAppointementView.as_view(), name="edit_appointement"),
    path('appointment/add', addAppointment.AddAppointment.as_view(), name="add_appointment"),
    path('appointment/restore/<int:pk>',
         restoreAppointment.RestoreAppointementView.as_view(), name="restore_appointment"),
    ### Prescription ###
    path('prescription/', prescriptionView.PrescriptionView.as_view(), name="prescription"),
    path('prescription/add', addPrescriptionView.AddPrescriptionView.as_view(), name="prescription_add"),
    path('prescription/detail/<int:pk>',
         detailPrescriptionView.DetailPrescriptionView.as_view(), name="prescription_detail"),
    path('prescription/delete/<int:pk>',
         deletePrescriptionView.DeletePrescriptionView.as_view(), name="prescription_delete"),
    path('prescription/edit/<int:pk>', editPrescriptionView.EditPrescriptionView.as_view(), name="prescription_edit"),
    path('prescription/restore/<int:pk>',
         restorePrescriptionView.RestorePrescriptionView.as_view(), name="prescription_restore"),
    ### Patients ###
    path('patients', patientsView.PatientsView.as_view(), name="patients_view"),
    path('patient/<int:pk>', patientView.PatientView.as_view(), name="patient_view"),
    path('patient/<int:pk>/diseases', patientDiseasesView.PatientDiseasesView.as_view(), name="patient_diseases_view"),
    path('patient/<int:pk>/treatments', patientTreatmentsView.PatientTreatmentsView.as_view(),
         name="patient_treatments_view"),
    ### Settings ###
    path('settings/', SettingsView.as_view(), name="settings"),
    path('settings/delete', DeleteView.as_view(), name="delete"),
    path('settings/password', ChangePasswordView.as_view(), name="password_change"),
    path('settings/password_success', passwordSuccess, name="password_success"),
    path('settings/custom_profile_picture', CustomProfilePicture.as_view(), name="custom_profile_picture"),

]
