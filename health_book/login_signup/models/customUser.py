from django.db import models
from django.contrib.auth.models import AbstractUser
from login_signup.models.diseases import Diseases
from login_signup.models.doctor import Doctor
from login_signup.models.treatment import Treatment


class CustomUser(AbstractUser):

    MEDICAL_USER = "MEDICAL_USER"
    PATIENT = "PATIENT"

    ROLE_CHOICES = (
        (MEDICAL_USER, "Medical User"),
        (PATIENT, "Patient"),
    )

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
    role = models.CharField(max_length=12, choices=ROLE_CHOICES, default=PATIENT, verbose_name="Rôle")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('username').validators = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        permissions = (
            ("can_use_medical_stuff", "Can use medical stuff"),
        )
