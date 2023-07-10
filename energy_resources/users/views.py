from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import UserData
from .serializer import ChangePasswordSerializer, RegisterUserSerializer, UserIdentitySerializer


class ChangePasswordAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserData.objects.all()
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user


class UserIdentityAPIView(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserIdentitySerializer

    def get_object(self):
        return self.request.user


class RegisterAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer
