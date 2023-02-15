from django.urls import path

from users.views import UserUpdateAPIView, UserRetrieveAPIView

urlpatterns = [
    path('update/<int:pk>/', UserUpdateAPIView.as_view()),
    path('profile/<int:pk>/', UserRetrieveAPIView.as_view())
]
