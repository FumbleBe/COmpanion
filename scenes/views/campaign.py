from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from companion.api.mixins import MultipleSerializerMixin
from companion.api.permissions import IsDmOnly
from scenes.models import Campaign
from scenes.serializers import CampaignListSerializer, CampaignDetailSerializer


class CampaignViewset(MultipleSerializerMixin, ModelViewSet):
    queryset = Campaign.objects.all().order_by("starting_date")
    serializer_class = CampaignListSerializer
    detail_serializer_class = CampaignDetailSerializer

    permission_classes = [IsAuthenticated, IsDmOnly]
