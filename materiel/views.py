from django.shortcuts import render, redirect
from .models import Materiel
from .forms import MaterielForm
from django.shortcuts import get_object_or_404
from .models import Personnel,Materiel,Affectation,Reparation
def materiel_list(request):
    materiels = Materiel.objects.all()
    return render(request, 'materiel/liste.html', {'materiels': materiels})
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

def supprimer_materiel(request, pk):
    materiel=get_object_or_404(Materiel, pk=pk)
    if request.method == 'POST':
        materiel.delete()
        return redirect('materiel_list')
    return render(request, 'materiel/supprimer.html', {'materiel': materiel})
def affecter_materiel(request):
    materiels=Materiel.objects.all()
    personnels=Personnel.objects.all()
    if request.method=='POST':
        materiel_id = request.POST['materiel']
        personnel_id = request.POST['personnel']
        Affectation.objects.create(materiel_id=materiel_id, personnel_id=personnel_id, date_affectation=timezone.now())
        return redirect('materiel_list')
    return render(request, 'materiel/affecter.html', {'materiels': materiels, 'personnels': personnels})
def reparation_materiel(request):
    materiels=Materiel.objects.all()
    if request.method=='POST':
        materiel_id = request.POST['materiel']
        description = request.POST['description']
        Reparation.objects.create(materiel_id=materiel_id, description=description, date_reparation=timezone.now())
        return redirect('materiel_list')
    return render(request, 'materiel/reparation.html', {'materiels': materiels})
from .models import Materiel, Personnel, Affectation, Reparation

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
       
    


    


