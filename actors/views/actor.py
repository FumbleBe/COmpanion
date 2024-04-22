from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from companion.api.permissions import IsDmOrReadOnly
from django.utils.text import slugify

from companion.api.mixins import MultipleSerializerMixin
from actors.models import Character, NPC, Encounter, Capacity
from actors.serializers import (
    CharacterListSerializer,
    CharacterDetailSerializer,
    NPCListSerializer,
    NPCDetailSerializer,
    EncounterListSerializer,
    EncounterDetailSerializer
)


def copy_capacities_to_actor(capacity, path, actor):
    known_capacity = Capacity()

    for field in capacity._meta.fields:
        field_name = field.name
        field_value = getattr(capacity, field_name)
        if field_name != "id":
            setattr(known_capacity, field_name, field_value)

    known_capacity.actor = actor
    known_capacity.path = path
    known_capacity.save()


class CharacterViewset(MultipleSerializerMixin, ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterListSerializer
    detail_serializer_class = CharacterDetailSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.groups.filter(name="DungeonMaster").exists():
            return Character.objects.all()
        else:
            return Character.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save()  # Save the object
        profile = instance.profile
        for path in profile.paths.all():
            for capacity in path.capacities.all():
                copy_capacities_to_actor(capacity, path, instance)
        return Response(CharacterDetailSerializer(instance).data)


class NPCViewset(MultipleSerializerMixin, ModelViewSet):
    queryset = NPC.objects.all()
    serializer_class = NPCListSerializer
    detail_serializer_class = NPCDetailSerializer

    permission_classes = [IsAuthenticated, IsDmOrReadOnly]

    def get_queryset(self):
        if self.request.user.groups.filter(name="DungeonMaster").exists():
            return NPC.objects.all()
        else:
            return NPC.objects.filter(
                access__in=[self.request.user]
            ) | NPC.objects.filter(access__isnull=True)

    def perform_create(self, serializer):
        instance = serializer.save()  # Save the object
        profile = instance.profile
        for path in profile.paths.all():
            for capacity in path.capacities.all():
                copy_capacities_to_actor(capacity, path, instance)
        return Response(NPCDetailSerializer(instance).data)


class EncounterViewset(MultipleSerializerMixin, ModelViewSet):
    queryset = Encounter.objects.all()
    serializer_class = EncounterListSerializer
    detail_serializer_class = EncounterDetailSerializer

    permission_classes = [IsAuthenticated, IsDmOrReadOnly]

    def get_queryset(self):
        if self.request.user.groups.filter(name="DungeonMaster").exists():
            return Encounter.objects.all()
        else:
            return Encounter.objects.filter(
                access__in=[self.request.user]
            ) | Encounter.objects.filter(access__isnull=True)
            

    def perform_create(self, serializer):
        instance = serializer.save()  # Save the object
        paths = instance.path.all()
        for path in paths:
            for capacity in path.capacities.all():
                copy_capacities_to_actor(capacity, path, instance)
        
        return Response(EncounterDetailSerializer(instance).data)
