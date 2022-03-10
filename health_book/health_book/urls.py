from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from login_signup.views.indexView import IndexView
from login_signup.views.loginView import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('signup/', include('login_signup.urls')),
    path('home/', include('home.urls'), name='home'),
    path('login/', LoginView.as_view(), name="login"),
    path('', include('django.contrib.auth.urls')),
    path('sw.js/', TemplateView.as_view(template_name='sw.js',
         content_type='application/javascript'), name='sw.js'),
]

handler404 = "health_book.views.page_not_found"


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
