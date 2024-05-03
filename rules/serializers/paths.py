from rest_framework import serializers
from django.utils.text import slugify

from rules.models import Path, PathCapacity
from rules.serializers import CapacityListSerializer


class PathCapacitySerializer(serializers.ModelSerializer):
    rank = serializers.IntegerField()
    capacity = CapacityListSerializer()

    class Meta:
        model = PathCapacity
        fields = ["rank", "capacity"]


class PathListSerializer(serializers.ModelSerializer):
    capacities = PathCapacitySerializer(many=True, source="pathcapacity_set")
    # capacities = CapacityListSerializer(many=True, read_only=True)
    # slug = serializers.SlugField(read_only=True)

    # def create(self, validated_data):
    #     validated_data["slug"] = slugify(validated_data["name"])
    #     return super(PathListSerializer, self).create(validated_data)

    class Meta:
        model = Path
        fields = ["id", "name", "slug", "description", "capacities"]


class PathDetailSerializer(serializers.ModelSerializer):
    capacities = CapacityListSerializer(many=True, read_only=True)
    # slug = serializers.SlugField(read_only=True)

    # def create(self, validated_data):
    #     validated_data["slug"] = slugify(validated_data["name"])
    #     return super(PathDetailSerializer, self).create(validated_data)

    class Meta:
        model = Path
        fields = "__all__"
