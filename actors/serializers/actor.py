from rest_framework import serializers

from actors.models import Character


class CharacterListSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    species = serializers.StringRelatedField()
    profile = serializers.StringRelatedField()
    class Meta:
        model = Character
        fields = ['owner', 'name', 'level', 'gender', 'species', 'profile']

class CharacterDetailSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Character
        fields = '__all__'
