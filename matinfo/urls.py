from django.contrib import admin
from django.urls import path
from materiel import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('materiel/', views.materiel_list, name='materiel_list'),
    path('', views.materiel_list),  # 🔥 page d'accueil
    path('materiel/ajouter/', views.ajouter_materiel, name='ajouter_materiel'),
    path('materiel/modifier/<int:pk>/', views.modifier_materiel, name='modifier_materiel'),
    path('materiel/supprimer/<int:pk>/', views.supprimer_materiel, name='supprimer_materiel'),
    path('materiel/affecter/', views.affecter_materiel, name='affecter_materiel'),
    path('materiel/reparation/', views.reparation_materiel, name='reparation_materiel'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
]