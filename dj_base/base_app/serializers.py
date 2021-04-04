from django.contrib.auth.models import User
from rest_framework import serializers 
from rest_framework.permissions import IsAuthenticated
class UserSerializer(serializers.ModelSerializer):

    permission_classes = [IsAuthenticated];

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'last_login', 'is_staff', 'is_active', 'is_superuser' ]