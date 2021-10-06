from django.urls import path, include
from .views import index, home, logout


urlpatterns = [
    path('', index),
    path('accounts/', include('allauth.urls')),
    path('accounts/home/', home),
    path('accounts/log-out/', logout),
]