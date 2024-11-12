from rest_framework.serializers import ModelSerializer, SerializerMethodField, URLField

from materials.models import Course, Lessons
from materials.validators import URLCorrectValidator

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lessons
        fields = "__all__"
        validators = [URLCorrectValidator(field="url", url="https://www.youtube.com/")]

class CourseDetailSerializer(ModelSerializer):
    count_lessons = SerializerMethodField()
    lessons = LessonSerializer(many=True)

    def get_count_lessons(self, instance):
        return Lessons.objects.filter(course=instance).count()

    class Meta:
        model = Course
        fields = "__all__"

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


