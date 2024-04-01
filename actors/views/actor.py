from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from companion.api.mixins import MultipleSerializerMixin
from actors.models import Character
from actors.serializers import CharacterListSerializer, CharacterDetailSerializer


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
