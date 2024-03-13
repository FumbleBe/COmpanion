from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from actors.permissions import IsAdminAuthenticated, IsStaffAuthenticated
from actors.models import *
from actors.serializers import *


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == "retrieve" and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()



class CharacterViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = CharacterListSerializer
    # detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        return Character.objects.all()

    # @action(detail=True, methods=["post"])
    # def disable(self, request, pk):
    #     self.get_object().disable()
    #     return Response()
