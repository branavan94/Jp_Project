from rest_framework import viewsets
from .serializers import EventSerializer, FashionSerializer,One_to_OneSerializer,ActivitySerializer, ConciergeSerializer, ChauffeurSerializer, HotelSerializer, PlanningSerializer, ClientSerializer, Hospitality_PackSerializer
from .models import Event, Fashion_House,One_to_One,Activity, Concierge, Chauffeur, Hotel, Planning, Client, Hospitality_Pack

class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

class FashionViewSet(viewsets.ModelViewSet):
    serializer_class = FashionSerializer
    queryset = Fashion_House.objects.all()

class One_to_OneViewSet(viewsets.ModelViewSet):
    serializer_class = One_to_OneSerializer
    queryset = One_to_One.objects.all()
class ActivityViewSet(viewsets.ModelViewSet):
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()

class ConciergeViewSet(viewsets.ModelViewSet):
    serializer_class = ConciergeSerializer
    queryset = Concierge.objects.all()

class ChauffeurViewSet(viewsets.ModelViewSet):
    serializer_class = ChauffeurSerializer
    queryset = Chauffeur.objects.all()
class HotelViewSet(viewsets.ModelViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

class PlanningViewSet(viewsets.ModelViewSet):
    serializer_class = PlanningSerializer
    queryset = Planning.objects.all()
class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class Hospitality_PackViewSet(viewsets.ModelViewSet):
    serializer_class = Hospitality_PackSerializer
    queryset = Hospitality_Pack.objects.all()



