from rest_framework import serializers

from django.contrib.auth.models import User
from items.models import Item


class ItemListSerializer(serializers.ModelSerializer):
    # access = serializers.MultipleChoiceField(choices=[('all'),('all')],allow_blank=True)

    class Meta:
        model = Item
        fields = "__all__"
        # fields = ["name", "level", "gender", "species", "profile"]


class ItemDetailSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Item
        fields = "__all__"
