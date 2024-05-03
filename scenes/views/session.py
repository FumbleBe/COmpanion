from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# from companion.api.mixins import MultipleSerializerMixin
from companion.api.permissions import IsDmOnly
from scenes.models import Session
from scenes.serializers import SessionSerializer


class SessionViewset(ModelViewSet):
    queryset = Session.objects.all().order_by("date")
    serializer_class = SessionSerializer
    permission_classes = [IsAuthenticated, IsDmOnly]
