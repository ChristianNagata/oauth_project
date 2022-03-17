from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/my_articles/', views.my_articles, name='my_articles')
]