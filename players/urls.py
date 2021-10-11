from django.urls import path
from .views import playerAPIView


urlpatterns = [
    path('player/', playerAPIView.as_view()),
    path('player/<int:id>/', playerAPIView.as_view()),
]