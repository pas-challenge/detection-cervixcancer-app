from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Zone(models.Model):

    localite = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.localite

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Zone'
        verbose_name_plural = 'Zones'


class Service(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Docteur(models.Model):
    telephone = models.CharField(max_length=50, blank=True)
    hopital = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    zones = models.ManyToManyField(Zone, related_name="zones")
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Docteur'
        verbose_name_plural = 'Docteurs'


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'


class Diagnostic(models.Model):
    image = models.ImageField(upload_to="cervix-images", blank=True)
    prediction = models.IntegerField()
    validated = models.BooleanField(default=False)
    doneAt = models.DateTimeField(auto_now_add=True)
    dateModify = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.prediction)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Diagnostic'
        verbose_name_plural = 'Diagnostic'


class Dossier(models.Model):
    numero = models.CharField(max_length=50)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    docteur = models.ForeignKey(Docteur, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    diagnostic = models.ManyToManyField(Diagnostic)

    def __str__(self):
        return self.numero

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Dossier'
        verbose_name_plural = 'Dossiers'
