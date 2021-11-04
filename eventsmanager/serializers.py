from rest_framework import serializers
from .models import events

class eventsSerializer(serializers.ModelSerializer):

        class Meta:
                model = events
                fields = '__all__'


class aeventsSerializer(serializers.ModelSerializer):

        class Meta:
                model = events
                fields = ["title", "date"]

