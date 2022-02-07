from django.urls import path
from login_signup import views

app_name = 'login_signup'
urlpatterns = [
    path('<int:number>/', views.SignupView.as_view(), name="signup"),
]
