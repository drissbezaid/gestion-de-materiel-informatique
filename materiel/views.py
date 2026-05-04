from django.shortcuts import render, redirect
from .models import Materiel
from .forms import MaterielForm
from django.shortcuts import get_object_or_404
from .models import Personnel,Materiel,Affectation,Reparation
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
@login_required
def materiel_list(request):
    materiels = Materiel.objects.all()
    return render(request, 'materiel/liste.html', {'materiels': materiels})
@login_required
def ajouter_materiel(request):
    if request.method == 'POST':
        form = MaterielForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materiel_list')   
    else:
        form = MaterielForm()

    return render(request, 'materiel/ajouter.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404

@login_required
def modifier_materiel(request, pk):
    materiel = get_object_or_404(Materiel, pk=pk)

    if request.method == 'POST':
        form = MaterielForm(request.POST, instance=materiel)
        if form.is_valid():
            form.save()
            return redirect('materiel_list')  
    else:
        form = MaterielForm(instance=materiel)

    return render(request, 'materiel/modifier.html', {'form': form})

@login_required
def supprimer_materiel(request, pk):
    materiel=get_object_or_404(Materiel, pk=pk)
    if request.method == 'POST':
        materiel.delete()
        return redirect('materiel_list')
    return render(request, 'materiel/supprimer.html', {'materiel': materiel})
@login_required
def affecter_materiel(request):
    materiels=Materiel.objects.all()
    personnels=Personnel.objects.all()
    if request.method=='POST':
        materiel_id = request.POST['materiel']
        personnel_id = request.POST['personnel']
        Affectation.objects.create(materiel_id=materiel_id, personnel_id=personnel_id, date_affectation=timezone.now())
        materiel=Materiel.objects.get(id=materiel_id)
        materiel.statut='affecté'
        materiel.save()
        return redirect('materiel_list')
    return render(request, 'materiel/affecter.html', {'materiels': materiels, 'personnels': personnels})
@login_required
def reparation_materiel(request):
    materiels=Materiel.objects.all()
    if request.method=='POST':
        materiel_id = request.POST['materiel']
        description = request.POST['description']
        cout=request.POST['cout']
        if not cout:
            cout=0
        Reparation.objects.create(materiel_id=materiel_id, description=description, cout=cout, date_reparation=timezone.now())
        materiel=Materiel.objects.get(id=materiel_id)
        materiel.statut='en réparation'
        cout=0
        materiel.save()
        return redirect('materiel_list')
    return render(request, 'materiel/reparation.html', {'materiels': materiels})
from .models import Materiel, Personnel, Affectation, Reparation

@login_required
def dashboard(request):
    context = {
        "total_materiel": Materiel.objects.count(),
        "total_personnel": Personnel.objects.count(),
        "total_affectations": Affectation.objects.count(),
        "total_reparations": Reparation.objects.count(),

        "materiel_disponible": Materiel.objects.filter(statut="disponible").count(),
        "materiel_affecte": Materiel.objects.filter(statut="affecte").count(),
        "materiel_reparation": Materiel.objects.filter(statut="reparation").count(),
    }

    return render(request, "materiel/dashboard.html", context)
def signup(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Identifiants incorrects")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "deconnexion réussie.")
    return redirect('login')


       
    



       
    


    


