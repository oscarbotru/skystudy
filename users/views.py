from rest_framework import generics

from users.models import User
from users.permissions import OwnProfileEditPermission
from users.serializers import UserSerializer, UserProfileInfoSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [OwnProfileEditPermission]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
