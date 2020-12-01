from rest_framework import serializers
from .models import Event, Fashion_House, One_to_One, Activity, Concierge, Chauffeur, Hotel, Planning, Client,Hospitality_Pack, Hospitality_Pack
class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ("title", "date_debut", "date_fin", "description", "place","fashion_name")

class FashionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fashion_House
        fields = ("fashion_name", "debrief_received")

class One_to_OneSerializer(serializers.ModelSerializer):

    class Meta:
        model = One_to_One
        fields = ("date", "salon","staff","title")

class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ("title", "date_act","supplier_name","adress","budget","real_price","cancelation_policy_deadline","cancelation_policy_fees","contact_name","phone_number","mail_adress","status","typ_act")

class ConciergeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Concierge
        fields = ("login", "mdp","name","last_name")

class ChauffeurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chauffeur
        fields = ("name", "last_name","langue","lieu_depart","lieu_arrivee","consigne","horaire_chauffeur")

class HotelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hotel
        fields = ("reservation_nb", "date_debut","date_fin","room_type","tarif","estimated_budget","paid_by_JP","paid_by_client","night_booked_jp","night_booked_client","welcome_pack_arrived")

class PlanningSerializer(serializers.ModelSerializer):

    class Meta:
        model = Planning
        fields = ("list_hotel","nights_booked","list_driver", "digital_planning","language","travel_fees","list_activities")

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ("name","last_name","zone", "contact_principal","langue","accompanied","title","budget_jour","budget_semaine","plan","date", "telephone", "date_arrival", "date_leave", "status")

class Hospitality_PackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospitality_Pack
        fields = ("collection","horaires_dispo_concierge","list_services", "welcome_pack","title")
