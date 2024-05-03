from rest_framework import serializers
from django.utils.text import slugify

from scenes.models import Campaign


class CampaignListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        # fields = ["id", "name", "slug", "description", "limited"]
        fields = ["id", "name", "image"]


class CampaignDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = "__all__"
