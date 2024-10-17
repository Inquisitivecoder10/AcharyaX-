from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('learning_path/<str:topic>/', views.learning_path, name='learning_path'),
]
