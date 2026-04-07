from rest_framework import viewsets
from .models import Courses
from .serializers import CoursesSerializer



class CoursesViewSet(viewsets.ModelViewSet): 
    queryset=Courses.objects.all()
    serializer_class=CoursesSerializer

    def get_queryset(self):
        return Courses.objects.all().order_by('finish_date')