from rest_framework.viewsets import ReadOnlyModelViewSet
# from actors.permissions import IsAdminAuthenticated, IsStaffAuthenticated
from rules.models import *
from rules.serializers import *
from rules.views import MultipleSerializerMixin


class SpeciesViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = SpeciesListSerializer
    detail_serializer_class = SpeciesDetailSerializer

    def get_queryset(self):
        return Species.objects.all()
