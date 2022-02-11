from django.contrib import admin
from django.urls import path, include
from login_signup import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('signup/', include('login_signup.urls')),
    path('home/', include('home.urls'), name='home'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('', include('django.contrib.auth.urls')),
]

handler404 = "health_book.views.page_not_found"
