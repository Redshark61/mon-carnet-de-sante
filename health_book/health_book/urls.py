from django.contrib import admin
from django.urls import path, include
from login_signup import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', include('login_signup.urls')),
    path('home/', include('home.urls'), name='home'),
    path('login/', views.login, name="login"),
    path('', include('django.contrib.auth.urls')),
]
