from rest_framework import serializers

from course.models import Course, CourseChapter


class CourseListSerializer(serializers.HyperlinkedModelSerializer):
    number_of_chapters = serializers.SerializerMethodField()
    url_field_name = "course_detail"
    mentor = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Course
        # lookup_field = "slug"
        extra_kwargs = {"course_detail": {"lookup_field": "slug"}}
        fields = ["title", "mentor", "category",
                  "number_of_chapters", "course_detail"]

    def get_number_of_chapters(self, obj):
        return obj.chapters.count()


class CourseChapterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseChapter
        fields = ["chapter_title"]


class CourseDetailSerializer(serializers.ModelSerializer):

    chapters = CourseChapterSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = "__all__"
