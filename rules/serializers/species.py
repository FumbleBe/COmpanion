from rest_framework import serializers

from rules.models import *


class SpeciesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Species
        fields = "__all__"
