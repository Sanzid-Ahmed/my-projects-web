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
from rest_framework import status
from .models import Profile
from events.models import Event
from .serializers import ProfileSerializer

class MyProfileView(APIView):
    """
    Handles GET and PATCH requests for the current user's profile.
    """

    def get_object(self, request):
        """Return the profile for the current user."""
        # Adjust this if you have multiple users
        return Profile.objects.first()

    def get(self, request):
        profile = self.get_object(request)
        if not profile:
            return Response({"error": "Profile not found"}, status=404)

        events = Event.objects.all()

        # Count running and finished tasks
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

        data = ProfileSerializer(profile).data
        data.update({
            "running_tasks_count": running_events_count,
            "finished_tasks_count": finished_events_count,
            "normal_tasks_count": normal_events_count,
            "event_tasks_count": event_events_count,
            "assignment_tasks_count": assignment_events_count,
            "project_tasks_count": project_events_count,
            "finished_normal_tasks_count": finished_normal_events_count,
            "finished_event_tasks_count": finished_event_events_count,
            "finished_assignment_tasks_count": finished_assignment_events_count,
            "finished_project_tasks_count": finished_project_events_count,
        })

        return Response(data)

    def patch(self, request):
        """
        Handle coin exchanges or profile updates.
        Accepts partial updates.
        """
        profile = self.get_object(request)
        if not profile:
            return Response({"error": "Profile not found"}, status=404)

        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)



