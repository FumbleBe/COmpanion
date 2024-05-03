from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.http import Http404

from companion.api.mixins import MultipleSerializerMixin
from companion.api.permissions import IsDmOnly
from scenes.models import Chapter, Scene, Campaign
from scenes.serializers import ChapterSerializer, SceneListSerializer, SceneDetailSerializer


class ChapterViewset(ModelViewSet):
    queryset = Chapter.objects.all().order_by("name")
    serializer_class = ChapterSerializer

    permission_classes = [IsAuthenticated, IsDmOnly]

    def get_queryset(self):
        campaign_id = self.kwargs["campaign_id"]
        campaign = get_object_or_404(Campaign, id=campaign_id)
        if campaign_id is not None:
            if self.request.user.groups.filter(name="DungeonMaster").exists():
                return Chapter.objects.filter(campaign=campaign)
            else:
                raise Http404
        else:
            raise Http404

    def perform_create(self, serializer):
        campaign_id = self.kwargs["campaign_id"]
        campaign = get_object_or_404(Campaign, id=campaign_id)
        serializer.save(campaign=campaign)  # Attach the chapter to the campaign


class SceneViewset(MultipleSerializerMixin, ModelViewSet):
    queryset = Scene.objects.all().order_by("chapter", "order")
    serializer_class = SceneListSerializer
    detail_serializer_class = SceneDetailSerializer

    permission_classes = [IsAuthenticated, IsDmOnly]
