from django.urls import path, include
from .views import index, signup

urlpatterns = [
    path('', index),
    path('signup/', signup, name='signup'),

   
]