from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('HomePage/', views.homePage, name='sapp-homepage'),
    path('profile/', views.profile, name='sapp-profile'),
    path('login/', auth_view.LoginView.as_view(template_name='sapp/login.html'),
         name='sapp-loginPage'),
    path('logout/', auth_view.LogoutView.as_view(template_name='sapp/logout.html'),
         name='sapp-logoutPage'),
    path('logout/', views.login, name='sapp-logout'),
    path('signup/', views.signup, name='sapp-signup'),
    path('terms/', views.terms, name='sapp-terms'),
    path('', views.welcome, name='sapp-welcome'),
    path('view_pdf', views.view_pdf, name='sapp-view_pdf'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
