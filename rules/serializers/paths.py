from rest_framework import serializers

from rules.models import Path
from rules.serializers import CapacityListSerializer


class PathListSerializer(serializers.ModelSerializer):
    capacities = CapacityListSerializer(many=True, read_only=True)
    class Meta:
        model = Path
        fields = ["name", "description", "capacities"]


class PathDetailSerializer(serializers.ModelSerializer):
    capacities = CapacityListSerializer(many=True, read_only=True)
    class Meta:
        model = Path
        fields = "__all__"
