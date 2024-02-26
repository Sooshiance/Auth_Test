from rest_framework import response, status, permissions, generics
from rest_framework_simplejwt import tokens

from .serializers import *


class HomeAPIView(generics.GenericAPIView):
    """
    An end point for Home 
    """
    def get(self, request, *args, **kwargs):
        return response.Response(data=request.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        return response.Response(data=request.data, status=status.HTTP_200_OK)


class UserRegisterationAPIView(generics.GenericAPIView):
    """
    An endpoint for the client to create a new User.
    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = tokens.RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return response.Response(data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(generics.GenericAPIView):
    """
    An endpoint to authenticate existing users using their email and password.
    """

    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = CustomUserSerializer(user)
        token = tokens.RefreshToken.for_user(user)
        data = serializer.data
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return response.Response(data, status=status.HTTP_200_OK)
