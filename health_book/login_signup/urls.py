from django.urls import path
from .views.signupView import SignupView

app_name = 'login_signup'
urlpatterns = [
    path('<int:number>/', SignupView.as_view(), name="signup"),
]
