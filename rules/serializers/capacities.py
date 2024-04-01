from rest_framework import serializers

from rules.models import *


class CapacityListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Capacity
        fields = ["name", "description", "limited"]


class CapacityDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Capacity
        fields = "__all__"
