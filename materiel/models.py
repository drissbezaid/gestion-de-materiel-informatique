from django.db import models
class Personnel(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.nom + " " + self.prenom
class Materiel(models.Model):
    statut=[
        ('disponible', 'Disponible'),
        ('affecté', 'Affecté'),
        ('en réparation', 'En réparation'),
    ]
    nom=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    date_achat=models.DateField()
    etat=models.CharField(max_length=100, choices=[('en service', 'En service'), ('en panne', 'En panne'), ('en réparation', 'En réparation')])
    statut=models.CharField(max_length=20, choices=statut, default='disponible')
    def __str__(self):
        return self.nom
class Affectation(models.Model):
    personnel=models.ForeignKey(Personnel,on_delete=models.CASCADE)
    materiel=models.ForeignKey(Materiel,on_delete=models.CASCADE)
    date_affectation=models.DateField()
    date_retour=models.DateField(null=True, blank=True)
    def __str__(self):
        return self.personnel.nom + " " + self.personnel.prenom + " - " + self.materiel.nom
class Reparation(models.Model):
    materiel=models.ForeignKey(Materiel,on_delete=models.CASCADE)
    date_reparation=models.DateField()
    description=models.TextField(max_length=500)
    cout=models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.materiel.nom + " - " + str(self.date_reparation)


    # Create your models here.
