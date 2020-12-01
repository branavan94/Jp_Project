# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, FashionViewSet, One_to_OneViewSet,ActivityViewSet, ConciergeViewSet, ChauffeurViewSet, HotelViewSet, PlanningViewSet, ClientViewSet, Hospitality_PackViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'Fashion', FashionViewSet)
router.register(r'One to One', One_to_OneViewSet)
router.register(r'Activity', ActivityViewSet)
router.register(r'Concierge', ConciergeViewSet)
router.register(r'Chauffeur', ChauffeurViewSet)
router.register(r'Hotel', HotelViewSet)
router.register(r'Planning', PlanningViewSet)
router.register(r'Client', ClientViewSet)
router.register(r'Hospitality_Pack', Hospitality_PackViewSet)




urlpatterns = [
    path("", include(router.urls))
]
