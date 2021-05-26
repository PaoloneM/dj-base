from django.urls import path
from django.urls import include
from django.views.decorators.csrf import csrf_exempt

from .views import (
    UserGenericAPIView
)

urlpatterns = [
    path('user', UserGenericAPIView.as_view()),
    path('user/<str:pk>', csrf_exempt(UserGenericAPIView.as_view())),
]
