from rest_framework import serializers

from materails.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = (
            'pk',
            'title',
            'description'
        )


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'pk',
            'course',
            'title',
            'description',
            'video_link'
        )
