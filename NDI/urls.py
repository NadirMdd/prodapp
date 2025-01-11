from django.contrib import admin
from django.urls import path, include
from listings import views
from listings.views import ClientViewSet, CamionViewSet, OptionViewSet, BenneViewSet, CommandeViewSet
from rest_framework.routers import DefaultRouter

#django.urls.path : Utilisé pour définir des routes simples avec des vues associées.
#DefaultRouter : Un routeur Django REST Framework (DRF) pour gérer automatiquement les routes des API REST.
#-------------------------------------------------------------------------------------------------------
router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'camions', CamionViewSet)  
router.register(r'options', OptionViewSet)  
router.register(r'bennes', BenneViewSet)  
router.register(r'commandes', CommandeViewSet)  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('About-us/', views.about, name='about-us'),
    path('contact-us/', views.contact, name='contact'),
    path('api/', include(router.urls)),
    path('commande/', views.commande, name='commande'),
    path('home/', views.home, name='home'),
    path('commande/creer/', views.commandes_en_cours, name='creer_commande'),
    path('planning/', views.tps_travail, name='planning'),
]