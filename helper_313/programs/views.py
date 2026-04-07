from rest_framework import viewsets
from .models import Programs
from .serializers import ProgramsSerializer



class ProgramsViewSet(viewsets.ModelViewSet): 
    queryset=Programs.objects.all()
    serializer_class=ProgramsSerializer

    def get_queryset(self):
        return Programs.objects.all().order_by('finish_date')