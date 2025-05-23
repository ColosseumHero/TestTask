from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Incident
from .serializers import IncidentSerializer, GeoJSONIncidentSerializer

class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    @action(detail=False, methods=['get'])
    def geojson(self, request):
        active_incidents = Incident.objects.filter(status='ACTIVE')
        serializer = GeoJSONIncidentSerializer(active_incidents, many=True)
        return Response({
            "type": "FeatureCollection",
            "features": serializer.data
        })