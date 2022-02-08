from django.urls import path
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('diseases/', views.DiseasesView.as_view(), name="diseases"),
]
