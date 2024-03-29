from rest_framework import serializers

from .models import QueueItems, Room


class RoomSerializer(serializers.ModelSerializer):
    class meta:
        model = Room
        fields = "__all__"


class QueueItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueItems
        fields = "__all__"
