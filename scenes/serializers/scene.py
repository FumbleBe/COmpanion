from rest_framework import serializers
from scenes.models import Chapter, Scene


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = "__all__"


class SceneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scene
        fields = ("id", "title")


class SceneDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scene
        fields = "__all__"
