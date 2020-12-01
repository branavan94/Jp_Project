import os



def populate():

	#Fashion House

	f1 = Fashion_House(fashion_name="Chanel", debrief_received=False)
	f2 = Fashion_House(fashion_name="Dior", debrief_received=True)
	f3 = Fashion_House(fashion_name="Lancel", debrief_received=False)
	f4 = Fashion_House(fashion_name="Gucci", debrief_received=False)
	f5 = Fashion_House(fashion_name="LVMH", debrief_received=True)
	f6 = Fashion_House(fashion_name="Louis Vuitton", debrief_received=True)

	f1.save()
	f2.save()
	f3.save()
	f4.save()
	f5.save()
	f6.save()


	# Event

	e1=Event(title="Du style en croks", date_debut='2019-12-12T15:00:00Z', date_fin='2019-12-17T15:00:00Z', description="Bienvenue a notre événement voici un sommaire des activites :", place="Paris", fashion_name = f1)
	e2=Event(title="Hiver neige", date_debut='2020-11-12T15:00:00Z', date_fin='2020-11-17T15:00:00Z', description="Bienvenue a notre événement voici un sommaire des activites :", place="Russie", fashion_name = f2)
	
	e1.save()
	e2.save()


	#One_to_One

	o1=One_to_One(date='2019-12-12T15:00:00Z', salon=10, staff="Paul JP",title = e1)
	o2=One_to_One(date='2019-12-12T15:00:00Z', salon=10, staff="Marie JP", title = e2)
	o3=One_to_One(date='2019-12-12T15:00:00Z', salon=10, staff="Kevin JP", title = e1)
	o4=One_to_One(date='2019-12-12T15:00:00Z', salon=10, staff="Pierre JP", title = e2)


	o1.save()
	o2.save()
	o3.save()
	o4.save()




	#Activity


	a1=Activity(title="Restaut à la Giraffe ", date_act='2019-12-13T00:00:00Z', supplier_name="Chantal", adress="89 rue de rivoli", budget=100, real_price=150, cancelation_policy_deadline=48, cancelation_policy_fees=0.8, contact_name="Fabris", phone_number="0604157343", mail_adress="fabris.contact@ext.com", status="cf", typ_act="1" )
	a2=Activity(title="Tour Eiffel de nuit ", date_act='2019-12-15T00:00:00Z', supplier_name="Charly", adress="17 rue des étudiants", budget=200, real_price=0, cancelation_policy_deadline=72, cancelation_policy_fees=0.6, contact_name="Fabris", phone_number="0604157343", mail_adress="fabris.contact@ext.com", status="cnf", typ_act="2" )
	a3=Activity(title="Spa massage", date_act='2019-12-17T00:00:00Z', supplier_name="Joseph", adress="50 rue de rivoli", budget=1000, real_price=800, cancelation_policy_deadline=48, cancelation_policy_fees=0.5, contact_name="Fabris", phone_number="0604157343", mail_adress="fabris.contact@ext.com", status="f", typ_act="4")


	a1.save()
	a2.save()
	a3.save()


	#Concierge

	c1=Concierge(login="0001", mdp="0001", name="Jean",last_name="Concierge")
	c2=Concierge(login="0002", mdp="0002", name="Kevin",last_name="Concierge")
	c3=Concierge(login="0003", mdp="0003", name="Marie",last_name="Concierge")

	c1.save()
	c2.save()
	c3.save()
	c1.list_events.add(e1,e2)
	c2.list_events.add(e1)
	c3.list_events.add(e2)

	#Chauffeur
	 
	t1=Chauffeur(name="Karim", last_name="Uber", langue="Fr", lieu_depart="Paris Roissy", lieu_arrivee="Carlton", consigne="Ne pas perdre le client de vue", horaire_chauffeur='2019-12-12T15:00:00Z')

	t1.save()
	  

	#Hotel

	h1=Hotel(reservation_nb=5, date_debut='2019-12-12T15:00:00Z', date_fin='2019-12-12T15:00:00Z', room_type="Suite Deluxe", tarif=500, estimated_budget=550, paid_by_JP=2, paid_by_client=3, night_booked_jp=2, night_booked_client=3, welcome_pack_arrived=True)

	h1.save()


	#Planning 

	p1=Planning(nights_booked=5,  digital_planning=True, language="EN", travel_fees=500)
	p2=Planning(nights_booked=3, language="FR", travel_fees=500)
	p3=Planning(nights_booked=2,  digital_planning=True, language="EN", travel_fees=2000)
	p4=Planning(nights_booked=4,  digital_planning=True, language="EN", travel_fees=500)



	p2.save()
	p3.save()
	p4.save()
	p1.save()

	p1.list_activities.add(a1)
	p1.list_driver.add(t1)
	p1.list_hotel.add(h1)

	p2.list_activities.add(a2)
	p2.list_driver.add(t1)
	p2.list_hotel.add(h1)

	p3.list_activities.add(a3)
	p3.list_driver.add(t1)
	p3.list_hotel.add(h1)

	
	#Client 

	cl1=Client(name="Jacques", last_name="Dupont", zone="Asie", contact_principal="jhon@jp.com",langue="En", budget_jour=500, budget_semaine=5000, plan=p1, date=o1,telephone = "0664587985", date_arrival='2019-12-12T15:00:00Z', date_leave='2019-12-17T15:00:00Z', status = 'al')
	cl2 = Client(name = "Hiba", last_name = "Beldi", zone = "Moyen-Orient", langue= "Arabe", budget_jour = 150, budget_semaine = 1500, date = o2, plan=p2, telephone = "0664152465", date_arrival='2019-12-13T15:00:00Z', date_leave='2019-12-16T15:00:00Z', status = 'mn')
	cl3 = Client(name = "Jérémie", last_name = "Bencini", zone = "Arctique", langue= "Anglais", budget_jour = 3000, budget_semaine = 30000, date = o3, plan=p3, telephone = "0668358476", date_arrival='2019-12-11T15:00:00Z', date_leave='2019-12-19T15:00:00Z', status = 'mn')
	cl4 = Client(name = "Diane", last_name = "Du Peloux", zone = "Afrique", langue= "Français", budget_jour = 300, budget_semaine = 3000, date = o4, plan=p4, telephone = "0542487945", date_arrival='2019-12-14T15:00:00Z', date_leave='2019-12-20T15:00:00Z', status = 'al')

	cl1.save()
	cl2.save()
	cl3.save()
	cl4.save()



	cl1.title.add(e1)
	cl2.title.add(e1)
	cl3.title.add(e2)
	cl4.title.add(e2)




	#Hospitality_packs
	hp1 = Hospitality_Pack(collection = "Printemps 2020", horaires_dispo_concierge = "Lundi-Dimance: 7h-23h", title = e1)
	
	hp1.save()
	
	hp1.list_services.add(a1)
	

if __name__ == '__main__':
	import django
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
	django.setup()
	from core.models import Fashion_House, Event, One_to_One, Activity, Concierge,Chauffeur, Hotel, Planning, Client, Hospitality_Pack
	populate() 