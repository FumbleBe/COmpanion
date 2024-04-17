from rest_framework import serializers

from actors.models import Character, NPC, Encounter


class CharacterListSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    species = serializers.StringRelatedField()
    profile = serializers.StringRelatedField()
    class Meta:
        model = Character
        fields = ['owner', 'id', 'name', 'level', 'gender', 'species', 'profile']

class CharacterDetailSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Character
        fields = '__all__'


class NPCListSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = NPC
        fields = ["id", "name", "level", "gender", "species"]


class NPCDetailSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = NPC
        fields = "__all__"


class EncounterListSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Encounter
        fields = ["id", "name", "nc", "category", "archetype"]


class EncounterDetailSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Encounter
        fields = "__all__"
