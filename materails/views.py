from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from materails.models import Course, Lesson
from materails.permissions import ModeratorPermission, LessonPermission
from materails.serlializers import CourseSerializer, LessonSerializer


# Courses
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [ModeratorPermission]


# Lessons
class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [LessonPermission]


class LessonListAPIVIew(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
