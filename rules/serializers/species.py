from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)

from rules.models import *
from rules.serializers import PathListSerializer


class SpeciesListSerializer(ModelSerializer):

    class Meta:
        model = Species
        fields = ["id", "name", "img"]


class SpeciesDetailSerializer(ModelSerializer):

    paths = SerializerMethodField()

    class Meta:
        model = Species
        fields = "__all__"

    def get_paths(self, instance):
        queryset = instance.paths.all()
        serializer = PathListSerializer(queryset, many=True)
        return serializer.data
