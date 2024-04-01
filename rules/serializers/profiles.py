from rest_framework import serializers

from rules.models import *


class ProfileListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ["name", "img", "dv", "description", "source"]


class ProfileDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"
