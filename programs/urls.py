from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgramsViewSet

router = DefaultRouter()
router.register(r'programs', ProgramsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]