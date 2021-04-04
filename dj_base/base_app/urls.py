from django.urls import path

from .views import (
    UserGenericAPIView
)

urlpatterns = [
    path('user', UserGenericAPIView.as_view()),
]
