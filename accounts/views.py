
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from accounts.serializer import LoginSerializer
from rest_framework.decorators import api_view


@api_view(['POST'])
def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
