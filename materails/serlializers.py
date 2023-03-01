from rest_framework import serializers

from materails.models import Course, Lesson
from materails.validators import LinkValidator


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    # lessons = LessonInfoSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = (
            'pk',
            'title',
            'description',
            'lesson_count',
            # 'lessons'
        )

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()


class LessonSerializer(serializers.ModelSerializer):
    # course = CourseSerializer()
    class Meta:
        model = Lesson
        fields = (
            'pk',
            'course',
            'title',
            'description',
            'video_link'
        )
        validators = [LinkValidator(field='title')]


class LessonInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'pk',
            'title',
        )


