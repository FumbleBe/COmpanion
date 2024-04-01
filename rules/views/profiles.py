from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from companion.api.mixins import MultipleSerializerMixin
from companion.api.permissions import IsDmOrReadOnly
from rules.models import Profile
from rules.serializers import ProfileListSerializer, ProfileDetailSerializer


class ProfileViewset(MultipleSerializerMixin, ModelViewSet):
    queryset = Profile.objects.all().order_by('name')
    serializer_class = ProfileListSerializer
    detail_serializer_class = ProfileDetailSerializer

    permission_classes = [IsAuthenticated, IsDmOrReadOnly]
