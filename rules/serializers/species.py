from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField
)

from rules.models import Species
from rules.serializers import PathListSerializer, CapacityListSerializer


class SpeciesListSerializer(ModelSerializer):

    class Meta:
        model = Species
        fields = ["name", "img", "description", "source"]


class SpeciesDetailSerializer(ModelSerializer):

    paths = PathListSerializer(many=True, read_only=True)
    capacities = CapacityListSerializer(many=True, read_only=True)

    class Meta:
        model = Species
        fields = "__all__"

    # def get_paths(self, instance):
    #     queryset = instance.paths.all()
    #     serializer = PathListSerializer(queryset, many=True)
    #     return serializer.data
