from django.urls import path, include
from .views import index, home, user_login

urlpatterns = [
    path('', index, name='index'),
    path('login', user_login, name='login'),
    path('accounts/home/', home, name='home'),

]
