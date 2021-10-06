from django.urls import path, include
from .views import index, home


urlpatterns = [
    path('', index),
    path('accounts/', include('allauth.urls')),
    path('accounts/home/', home),
]