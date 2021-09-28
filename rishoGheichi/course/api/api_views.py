from django.utils import timezone

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from course.models import Course
from course.api.serializers import CourseListSerializer, CourseDetailSerializer


class CourseViewSet(ReadOnlyModelViewSet):

    queryset = Course.objects.all()

    lookup_field = "slug"

    serializer_class = {
        "list": CourseListSerializer,
        "retrieve": CourseDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializer_class.get(self.action)

    @action(detail=False, methods=["GET"], url_path="get-time")
    def get_time(self, request):
        return Response({"time": timezone.now()})
