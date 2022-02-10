from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Diseases(models.Model):

    name = models.CharField(max_length=100)
    symptoms = models.CharField(max_length=1000)
    cures = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name}"


class RPPS(models.Model):

    rpps = models.IntegerField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.rpps}"


class Job(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Location(models.Model):

    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.address}, {self.city} {self.postal_code}"


class Treatment(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Doctor(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rpps = models.ForeignKey(RPPS, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class CustomUser(AbstractUser):

    class Genders(models.TextChoices):
        MASCULIN = "M"
        FEMININ = "F"

    mail = models.EmailField(null=True)
    gender = models.CharField(max_length=1, choices=Genders.choices, null=True)
    main_doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL,
                                    null=True, related_name="User_main_doctor")
    parent1 = models.ForeignKey("self", on_delete=models.SET_NULL, null=True,
                                blank=True, related_name="User_parent1")
    parent2 = models.ForeignKey("self", on_delete=models.SET_NULL, null=True,
                                blank=True, related_name="User_parent2")
    birth_date = models.DateField(null=True)
    diseases = models.ManyToManyField(Diseases, through="UserDisease", related_name="User_disease")
    treatments = models.ManyToManyField(Treatment, related_name="User_treatment")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('username').validators = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class TrustedPerson(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class UserDisease(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    disease = models.ForeignKey(Diseases, on_delete=models.CASCADE)
    isCurrent = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} {self.disease}"


class Appointment(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    name = models.CharField(max_length=100)
    description = models.TextField()


class Prescription(models.Model):

    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    prescription = models.TextField()
    end_date = models.DateField(null=True, blank=True)
    is_permanent = models.BooleanField(default=False)
