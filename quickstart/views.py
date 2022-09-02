# Create your views here.

from quickstart.models import Airplane
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import AirplaneSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer


