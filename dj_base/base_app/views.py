from .serializers import UserSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class UserGenericAPIView(APIView):

    def get(self, request):
        userSer = UserSerializer(request.user)
        print(userSer.data)
        return Response({
                'data': userSer.data
            })
