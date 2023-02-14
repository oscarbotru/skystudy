from django.urls import path

from users.views import UserUpdateAPIView

urlpatterns = [
    path('update/<int:pk>/', UserUpdateAPIView.as_view())
]
