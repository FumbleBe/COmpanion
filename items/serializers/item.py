from rest_framework import serializers
from django.utils.text import slugify

from items.models import Item


class ItemListSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    def create(self, validated_data):
        validated_data["slug"] = slugify(
            validated_data["name"]
        )
        return super(ItemListSerializer, self).create(validated_data)

    class Meta:
        model = Item
        fields = "__all__"
        # fields = ["name", "level", "gender", "species", "profile"]


class ItemDetailSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Item
        fields = "__all__"
