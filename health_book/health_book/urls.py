from django.contrib import admin
from django.urls import path, include
from login_signup.views.indexView import IndexView
from login_signup.views.loginView import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('signup/', include('login_signup.urls')),
    path('home/', include('home.urls'), name='home'),
    path('login/', LoginView.as_view(), name="login"),
    path('', include('django.contrib.auth.urls')),
]

handler404 = "health_book.views.page_not_found"
