from django.db import models
from django.conf import settings
from login_signup.models.doctor import Doctor
from login_signup.models.diseases import Diseases
from login_signup.models.treatment import Treatment


class Prescription(models.Model):

    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, verbose_name='Médecin')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Patient')
    treatment = models.ForeignKey(Treatment, on_delete=models.SET_NULL, null=True, verbose_name='Traitement')
    diseases = models.ForeignKey(Diseases, on_delete=models.SET_NULL, null=True, verbose_name='Maladie')
    prescription = models.TextField(verbose_name='Informations complémentaire')
    end_date = models.DateField(null=True, blank=True, verbose_name='Date de fin')
    is_permanent = models.BooleanField(default=False, verbose_name='Est-ce permanent')
