from django.contrib import admin
from .models import *

# Register your models here.


class DocteurAdmin(admin.ModelAdmin):
    list_display = ('telephone', 'hopital', 'user', 'service')


admin.site.register(Docteur, DocteurAdmin)


class PatientAdmin(admin.ModelAdmin):
    list_display = ('telephone', 'adresse', 'age', 'user')


admin.site.register(Patient, PatientAdmin)


class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ('image', 'prediction', 'validated', 'doneAt', 'dateModify')


admin.site.register(Diagnostic, DiagnosticAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Service._meta.fields if field.name != "id"]


admin.site.register(Service, ServiceAdmin)


class DossierAdmin(admin.ModelAdmin):
    list_display = ('numero', 'patient', 'docteur', 'zone')


admin.site.register(Dossier, DossierAdmin)


class ZoneAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Zone._meta.fields if field.name != "id"]


admin.site.register(Zone, ZoneAdmin)
