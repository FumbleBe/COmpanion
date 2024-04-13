from rest_framework import serializers
from django.utils.text import slugify

from rules.models import *


class ProfileListSerializer(serializers.ModelSerializer):
    # slug = serializers.SlugField(read_only=True)

    # def create(self, validated_data):
    #     validated_data["slug"] = slugify(validated_data["name"])
    #     return super(ProfileListSerializer, self).create(validated_data)

    class Meta:
        model = Profile
        fields = ["id","name", "slug" ,"img", "dv", "description", "source"]


class ProfileDetailSerializer(serializers.ModelSerializer):
    # slug = serializers.SlugField(read_only=True)

    # def create(self, validated_data):
    #     validated_data["slug"] = slugify(validated_data["name"])
    #     return super(ProfileDetailSerializer, self).create(validated_data)

    class Meta:
        model = Profile
        fields = "__all__"
