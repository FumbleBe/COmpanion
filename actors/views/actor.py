from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from companion.api.permissions import IsDmOrReadOnly

from companion.api.mixins import MultipleSerializerMixin
from actors.models import Character, NPC, Encounter
from actors.serializers import (
    CharacterListSerializer,
    CharacterDetailSerializer,
    NPCListSerializer,
    NPCDetailSerializer,
    EncounterListSerializer,
    EncounterDetailSerializer
)


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
