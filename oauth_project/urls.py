from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from allauth.account.adapter import DefaultAccountAdapter

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view(), name='logout'),
    path('verification/', include('verify_email.urls')),
    path('conta/', include('user.urls')),
]
