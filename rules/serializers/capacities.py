from rest_framework import serializers
from django.utils.text import slugify

from rules.models import *


class CapacityListSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    def create(self, validated_data):
        validated_data["slug"] = slugify(validated_data["name"])
        return super(CapacityListSerializer, self).create(validated_data)

    class Meta:
        model = Capacity
        fields = ["name", "description", "limited"]


class CapacityDetailSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    def create(self, validated_data):
        validated_data["slug"] = slugify(validated_data["name"])
        return super(CapacityDetailSerializer, self).create(validated_data)

    class Meta:
        model = Capacity
        fields = "__all__"
