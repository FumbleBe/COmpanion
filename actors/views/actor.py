from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from companion.api.permissions import IsDmOrReadOnly
from django.shortcuts import get_object_or_404
from django.http import Http404

from companion.api.mixins import MultipleSerializerMixin
from actors.models import Actor, Character, NPC, Encounter, Capacity
from rules.models import PathCapacity
from rules.serializers import CapacityDetailSerializer
from actors.serializers import (
    CharacterListSerializer,
    CharacterDetailSerializer,
    CapacityListSerializer,
    NPCListSerializer,
    NPCDetailSerializer,
    EncounterListSerializer,
    EncounterDetailSerializer,
)


def copy_capacities_to_actor(capacity, path, actor):
    known_capacity = Capacity()

    for field in capacity._meta.fields:
        field_name = field.name
        field_value = getattr(capacity, field_name)
        if field_name != "id":
            setattr(known_capacity, field_name, field_value)

    rank_value = (
        PathCapacity.objects.filter(capacity=capacity, path=path)
        .values_list("rank", flat=True)
        .first()
    )
    known_capacity.actor = actor
    known_capacity.path = path
    known_capacity.rank = rank_value
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

    def perform_update(self, serializer):
        instance = serializer.save()  # Save the object
        profile = instance.profile
        for path in profile.paths.all():
            for capacity in path.capacities.all():
                copy_capacities_to_actor(capacity, path, instance)
        return Response(CharacterDetailSerializer(instance).data)


class CharacterCapacityViewset(ModelViewSet):
    queryset = Capacity.objects.all()
    serializer_class = CapacityListSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        actor_id = self.kwargs["actor_id"]
        actor = get_object_or_404(Actor, id=actor_id)
        if actor_id is not None:
            if self.request.user.groups.filter(name="DungeonMaster").exists():
                return Capacity.objects.filter(actor=actor)
            try:
                if self.request.user == actor.owner:
                    return Capacity.objects.filter(actor=actor)
                else:
                    raise Http404
            except AttributeError:
                raise Http404
        else:
            raise


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
