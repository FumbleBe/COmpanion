from rest_framework import serializers
from django.utils.text import slugify

from rules.models import Species
from rules.serializers import PathListSerializer, CapacityListSerializer


class SpeciesListSerializer(serializers.ModelSerializer):
    # slug = serializers.SlugField(write_only=True)

    # def create(self, validated_data):
    #     validated_data["slug"] = slugify(validated_data["name"])
    #     return super(SpeciesListSerializer, self).create(validated_data)

    class Meta:
        model = Species
        fields = ["id", "name", "slug", "img", "description", "source"]


class SpeciesDetailSerializer(serializers.ModelSerializer):
    # slug = serializers.SlugField(read_only=True)
    paths = PathListSerializer(many=True, read_only=True)
    capacities = CapacityListSerializer(many=True, read_only=True)

    # def create(self, validated_data):
    #     validated_data["slug"] = slugify(validated_data["name"])
    #     return super(SpeciesDetailSerializer, self).create(validated_data)

    class Meta:
        model = Species
        fields = "__all__"
        # exclude = ["slug"]
