from django.urls import path
from rest_framework.routers import DefaultRouter

from materails.views import CourseViewSet, LessonCreateAPIView, LessonRetrieveAPIView, LessonListAPIVIew, \
    LessonUpdateAPIView, LessonDestroyAPIView

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')


urlpatterns = [
    path('lesson/', LessonListAPIVIew.as_view()),
    path('lesson/create/', LessonCreateAPIView.as_view()),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view()),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view()),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view()),

              ] + router.urls
