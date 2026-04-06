from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

        # You could also list fields manually like:
        # fields = ['title', 'occur_date', 'status']