from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer, UserProfileInfoSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserProfileInfoSerializer
    queryset = User.objects.all()
