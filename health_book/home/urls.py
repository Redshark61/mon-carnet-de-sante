from django.urls import path
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('diseases/', views.DiseasesView.as_view(), name="diseases"),
    path('treatments/', views.TreatmentsView.as_view(), name="treatments"),
    path('settings/', views.SettingsView.as_view(), name="settings"),
    path('settings/delete', views.DeleteView.as_view(), name="delete"),
]
