from django.urls import path, include
from .views import index,dashboard

urlpatterns = [
    path('', index),
    path('dashboard/', dashboard, name='dashboard'),
]