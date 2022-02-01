from django.urls import path
from login_signup import views

app_name = 'login_signup'
urlpatterns = [
    path('<int:number>/', views.signup, name="signup"),
    path('medical/', views.signupMedical, name="signup_medical"),
    # path('medical/validate', views.medicalValidate, name="medical_validate"),
]
