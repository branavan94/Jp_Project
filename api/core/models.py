# core/models.py

from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Fashion_House(models.Model):
       fashion_name = models.CharField(verbose_name="Fashion House Name", max_length=120)
       debrief_received =  models.BooleanField(default=False)
       def __str_(self):
        	return self.fashion_name
        
class Event(models.Model):
        title = models.CharField(verbose_name="Event Name", max_length=120)
        date_debut = models.DateTimeField(default=timezone.now)
        date_fin = models.DateTimeField(default=timezone.now)
        description = models.TextField(blank=True)
        place = models.CharField(verbose_name="Event Place", max_length=120)
        fashion_name = models.ForeignKey(Fashion_House, default= None, verbose_name="Fashion House Name", on_delete=models.SET_DEFAULT)
        def __str_(self):
        	return "Recipe for {}".format(self.name)

class One_to_One(models.Model):
        date =  models.DateTimeField(default=timezone.now)
        salon = models.PositiveIntegerField(default = 0)
        staff = models.TextField(blank=True)
        title = models.ForeignKey(Event, on_delete=models.CASCADE, default = 0, verbose_name= "Event associated to")

class Activity(models.Model): #Ã©quivalent Ã  Treatment cost VOULEZ-VOUS UN HERITAGE OU SEPARER TAXI/HOTEL DES AUTRES ?
        title = models.CharField(verbose_name="Event Name", max_length=120)
        date_act =  models.DateTimeField(default=timezone.now)
        supplier_name = models.CharField(verbose_name="Supplier Name", max_length=120)
        adress = models.CharField(verbose_name="Google Map ID", max_length=500)
        budget = models.FloatField(default = 0)
        real_price = models.FloatField(default = 0)
        cancelation_policy_deadline = models.PositiveIntegerField()
        cancelation_policy_fees = models.FloatField() #pourcentage attention
        contact_name = models.CharField(verbose_name="Contact Name", max_length=120)
        phone_number = models.CharField(verbose_name="Event Name", max_length=120)
        mail_adress = models.EmailField(default = 'a@ext.com')
        paid = models.BooleanField(default=False)
        STATUS = (('cf', 'Cancelled and factured'), ('cnf', 'Cancelled and not factured'), ('f', 'Factured'), ('cn', 'Cancelled and negociated'),)
        status=models.CharField(max_length=10, choices=STATUS)
        TYP_ACT = (('1', 'Beauté'), ('2', 'Santé'), ('3', 'Bar'), ('4','Arts'), ('5','Autre'),)
        typ_act=models.CharField(max_length=1, choices=TYP_ACT)

class Concierge(models.Model):
        login = models.CharField('ID', max_length=120)
        mdp = models.CharField('Password', max_length=120)
        name = models.CharField('Concierge Name', max_length=120)
        last_name = models.CharField('Concierge Last Name', max_length=120)
        list_events = models.ManyToManyField(Event, verbose_name="list of events", default = 0)

class Chauffeur(models.Model):
        name = models.CharField(verbose_name="Driver Name", max_length=120)
        last_name = models.CharField(verbose_name="Driver Last Name", max_length=120)
        langue = models.CharField(verbose_name="Client Language", max_length=120)
        lieu_depart = models.TextField(blank=True)
        lieu_arrivee = models.TextField(blank=True)
        consigne = models.TextField(blank=True)
        photo = models.BooleanField(default=False)
        horaire_chauffeur =  models.DateTimeField(default=timezone.now)

class Hotel(models.Model):
        reservation_nb = models.PositiveIntegerField(default = 0)
        date_debut =  models.DateTimeField(default=timezone.now)
        date_fin =  models.DateTimeField(default=timezone.now)
        room_type = models.CharField('Hotel Name', max_length=120) #listbox ? vocabulaire des chambres ?
        cancellation = models.BooleanField(default=False)
        tarif = models.FloatField(default = 0)
        estimated_budget = models.FloatField(default = 0)
        paid_by_JP = models.FloatField(default = 0) #dans le cas oÃ¹ compris ds son voyage
        paid_by_client = models.FloatField(default = 0) #dans le cas oÃ¹ non compris dans le voyage
        night_booked_jp = models.PositiveIntegerField(default = 0)
        night_booked_client = models.PositiveIntegerField(default = 0)
        welcome_pack_arrived = models.BooleanField(default=False)

class Planning(models.Model):
        list_hotel = models.ManyToManyField(Hotel, verbose_name="list of hotels")
        nights_booked = models.PositiveIntegerField(default = 0)
        list_driver = models.ManyToManyField(Chauffeur, verbose_name="list of drivers")
        digital_planning = models.BooleanField(default=False)
        language = models.CharField('Client Language', max_length=120) #by default client language ?
        travel_fees = models.FloatField(default = 0)
        list_activities = models.ManyToManyField(Activity, verbose_name="list of activities")

class Client(models.Model):
        name = models.CharField('Client Name', max_length=120)
        last_name = models.CharField('Client Last Name', max_length=120)
        zone = models.CharField('Market Place', max_length=120)
        contact_principal = models.EmailField(default = 'test@jp.com')
        #mails_en_copie = []
        langue = models.CharField('Client Language', max_length=120)
        accompanied = models.BooleanField(default=False)
        title = models.ManyToManyField(Event, verbose_name="list of events")
        budget_jour = models.FloatField(default = 0)
        budget_semaine = models.FloatField(default = 0)
        plan = models.OneToOneField(Planning,on_delete=models.CASCADE, default = 0)
        date = models.ForeignKey(One_to_One, on_delete=models.CASCADE, default = 0,verbose_name = "Date of the One to One")
        telephone = models.CharField('Client Phone', max_length=120)
        date_arrival = models.DateTimeField(default =timezone.now)
        date_leave = models.DateTimeField(default=timezone.now)
        STATUS = (('mn', 'Modification Necessary'), ('al', 'All Good'))
        status=models.CharField(max_length=10, choices=STATUS)

class Hospitality_Pack(models.Model): #foreign key Ã©vÃ©nement id OU Client
        collection = models.TextField(blank=True) #dÃ©tails sur la collection
        horaires_dispo_concierge = models.TextField(blank=True)
        list_services = models.ManyToManyField(Activity, verbose_name="list of activities") 
        welcome_pack = models.TextField(blank=True) #Finalement bouton "parcourir"
        title = models.ForeignKey(Event, on_delete=models.CASCADE, default = 0)
      

