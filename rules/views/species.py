from rest_framework.viewsets import ReadOnlyModelViewSet
# from actors.permissions import IsAdminAuthenticated, IsStaffAuthenticated
from rules.models import *
from rules.serializers import *


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == "retrieve" and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class SpeciesViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = SpeciesListSerializer
    # detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        return Species.objects.all()

