from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView

from users.models import User
from users.serializers import UserSerializer, UserProfileInfoSerializer, PaymentSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserProfileInfoSerializer
    queryset = User.objects.all()


class PaymentListAPIVIew(ListAPIView):
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['lesson', 'course', 'pay_type']
    ordering_fields = ['datetime']
