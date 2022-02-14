from django.urls import path
from .views.appointmentsView import AppointmentsView
from .views.deleteView import DeleteView
from .views.diseaseView import DiseasesView
from .views.homeView import HomeView
from .views.passwordSuccess import passwordSuccess
from .views.settingsView import SettingsView
from .views.treatmentView import TreatmentsView
from .views.changePasswordView import ChangePasswordView
from .views.addDisease import AddDisease
from .views.deleteDisease import DeleteDisease
from .views.addTreatment import AddTreatment
from .views.deleteTreatment import DeleteTreatment

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('diseases/', DiseasesView.as_view(), name="diseases"),
    path('treatments/', TreatmentsView.as_view(), name="treatments"),
    path('settings/', SettingsView.as_view(), name="settings"),
    path('settings/delete', DeleteView.as_view(), name="delete"),
    path('settings/password', ChangePasswordView.as_view(), name="password_change"),
    path('settings/password_success', passwordSuccess, name="password_success"),
    path('appointments/', AppointmentsView.as_view(), name="appointments"),
    path('add_disease/', AddDisease.as_view(), name="add_disease"),
    path('delete_disease/<int:pk>', DeleteDisease.as_view(), name="delete_disease"),
    path('add_treatment/', AddTreatment.as_view(), name="add_treatment"),
    path('delete_treatment/<int:pk>', DeleteTreatment.as_view(), name="delete_treatment"),
]
