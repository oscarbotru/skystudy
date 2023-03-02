from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from materails.models import Course
from users.models import User, Subscription
from users.permissions import OwnProfileEditPermission
from users.serializers import UserSerializer, UserProfileInfoSerializer, SubscriptionSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [OwnProfileEditPermission]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class SubscriptionToggleAPIView(APIView):

    @swagger_auto_schema(responses={200: SubscriptionSerializer(many=True)})
    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data.get('course')
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item = Subscription.objects.filter(user=user, course=course_item)

        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'

        else:
            Subscription.objects.create(user=user, course=course_item)
            message = 'подписка добавлена'

        return Response({"message": message})
