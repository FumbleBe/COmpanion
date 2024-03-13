from rest_framework import serializers

from rules.models import *


class PathListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Path
        fields = "__all__"
