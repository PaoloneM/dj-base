from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import ProductGenericAPIView

urlpatterns = [
                  path('products', ProductGenericAPIView.as_view()),
                  path('products/<str:pk>', ProductGenericAPIView.as_view()),
              ]