from rest_framework import serializers

from actors.models import Character, NPC, Encounter, Capacity
from rules.models import Path
from rules.serializers import SpeciesDetailSerializer

# from rules.serializers 

class CapacityListSerializer(serializers.ModelSerializer):
    path = serializers.StringRelatedField()
    class Meta:
        model = Capacity
        fields = ["id", "path", "rank", "name", "slug", "description", "limited", "learned"]


class PathListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Path
        fields = ["id", "name"]


class CharacterListSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    species = serializers.StringRelatedField()
    profile = serializers.StringRelatedField()
    class Meta:
        model = Character
        fields = ['owner', 'id', 'name', 'level', 'gender', 'species', 'profile']

class CharacterDetailSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    capacities = CapacityListSerializer(many=True, read_only=True)
    species = SpeciesDetailSerializer(read_only=True)
    profile = serializers.StringRelatedField()
    class Meta:
        model = Character
        fields = '__all__'


class NPCListSerializer(serializers.ModelSerializer):
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = NPC
        fields = ["id", "name", "level", "gender", "species"]


class NPCDetailSerializer(serializers.ModelSerializer):
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    capacities = CapacityListSerializer(many=True, read_only=True)
    class Meta:
        model = NPC
        fields = "__all__"


class EncounterListSerializer(serializers.ModelSerializer):
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Encounter
        fields = ["id", "name", "nc", "category", "archetype"]


class EncounterDetailSerializer(serializers.ModelSerializer):
    # owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    capacities = CapacityListSerializer(many=True, read_only=True)
    capacity = CapacityListSerializer(many=True, read_only=True)
    path = PathListSerializer(many=True, read_only=True)
    class Meta:
        model = Encounter
        fields = "__all__"
