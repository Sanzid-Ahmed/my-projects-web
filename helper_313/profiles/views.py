# # profiles/views.py
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .models import Profile
# from .serializers import ProfileSerializer

# class ProfileViewSet(ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

#     def get_queryset(self):
#         # Only return the current user's profile
#         return Profile.objects.filter(user=self.request.user)

#     @action(detail=False, methods=['get'])
#     def me(self, request):
#         profile = self.get_queryset().first()
#         serializer = self.get_serializer(profile)
#         return Response(serializer.data)












# profiles/views.py
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Profile
# from .serializers import ProfileSerializer

# class MyProfileView(APIView):
#     def get(self, request):
#         # Get the first profile (your personal profile)
#         profile = Profile.objects.first()
#         if not profile:
#             return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)











# profiles/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from events.models import Event  # import your Event model
from .serializers import ProfileSerializer

class MyProfileView(APIView):
    def get(self, request):
        # get your personal profile
        profile = Profile.objects.first()
        if not profile:
            return Response({"error": "Profile not found"}, status=404)

        # get all events (all belong to you)
        events = Event.objects.all()

        # count running (upcoming or in-progress) and finished tasks
        normal_events_count = events.filter(task_type="normal", status__in=["upcoming", "pending"]).count()
        event_events_count = events.filter(task_type="event", status__in=["upcoming", "pending"]).count()
        assignment_events_count = events.filter(task_type="assignment", status__in=["upcoming", "pending"]).count()
        project_events_count = events.filter(task_type="project", status__in=["upcoming", "pending"]).count()

        
        finished_normal_events_count = events.filter(task_type="normal", status="finished").count()
        finished_event_events_count = events.filter(task_type="event", status="finished").count()
        finished_assignment_events_count = events.filter(task_type="assignment", status="finished").count()
        finished_project_events_count = events.filter(task_type="project", status="finished").count()
        
        running_events_count = events.filter(status__in=["upcoming", "pending"]).count()
        finished_events_count = events.filter(status="finished").count()

        # prepare profile data
        data = ProfileSerializer(profile).data

        data["running_tasks_count"] = running_events_count
        data["finished_tasks_count"] = finished_events_count

        data["normal_tasks_count"] = normal_events_count
        data["event_tasks_count"] = event_events_count
        data["assignment_tasks_count"] = assignment_events_count
        data[" project_tasks_count"] = project_events_count

        data["finished_normal_tasks_count"] = finished_normal_events_count
        data["finished_event_tasks_count"] = finished_event_events_count
        data["finished_assignment_tasks_count"] = finished_assignment_events_count
        data["finished_project_tasks_count"] = finished_project_events_count

        return Response(data)



