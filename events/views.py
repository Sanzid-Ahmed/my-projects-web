from rest_framework import viewsets
from datetime import date
from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self):
        today = date.today()

        # Update upcoming → pending
        Event.objects.filter(
            status="upcoming",
            # occur_date__lte=today   # old
            occur_date__lt=today    # new
        ).update(status="pending")

        # Return sorted data
        return Event.objects.all().order_by('occur_date')