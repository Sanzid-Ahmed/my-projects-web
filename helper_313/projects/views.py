from rest_framework import viewsets
from .models import Projects
from .serializers import ProjectsSerializer



class ProjectViewSet(viewsets.ModelViewSet): 
    queryset=Projects.objects.all()
    serializer_class=ProjectsSerializer

    def get_queryset(self):
        return Projects.objects.all().order_by('finish_date')