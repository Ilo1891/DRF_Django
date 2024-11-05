from rest_framework.serializers import ModelSerializer, SerializerMethodField, IntegerField

from materials.models import Course, Lessons

class CourseDetailSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()

    def get_count_lessons(self, instance):
        return len(Lessons.objects.filter(course=instance))

    class Meta:
        model = Course
        fields = "__all__"

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lessons
        fields = "__all__"
