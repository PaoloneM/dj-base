from rest_framework.authentication import SessionAuthentication
from .CsrfExemptSessionAuthentication import CsrfExemptSessionAuthentication
from .serializers import UserSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
class UserGenericAPIView(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication,)

    def get(self, request):
        userSer = UserSerializer(request.user)
        print(userSer.data)
        return Response({
                'data': userSer.data
            })

    def put(self, request, pk, format=None):
        user = User.objects.get(id =pk)
        userData = request.data
        serializer = UserSerializer(user, data=userData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
