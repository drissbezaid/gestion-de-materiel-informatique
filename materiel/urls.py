from django.urls import path
from . import views
urlpatterns=[
    path('admin/', views.admin, name='admin'),
    path('materiel/', views.materiel_list, name='materiel_list'),
    path('materiel/ajouter/', views.ajouter_materiel, name='ajouter_materiel'),
    path('materiel/modifier/<int:pk>/', views.modifier_materiel, name='modifier_materiel'),
    path('materiel/supprimer/<int:pk>/', views.supprimer_materiel, name='supprimer_materiel'),
    path('materiel/affecter/', views.affecter_materiel, name='affecter_materiel'),
    path('materiel/reparation/', views.reparation_materiel, name='reparation_materiel'),
    path('dashboard/', views.dashboard, name='dashboard'),

]