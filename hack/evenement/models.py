from django.db import models
from login.models import EmployeeAccount

class Evenement(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='images_evenements/')
    nom = models.CharField(max_length=100)
    organisation = models.CharField(max_length=100)
    lieu = models.CharField(max_length=100)
    date = models.DateField()
    description = models.CharField(max_length=1000)
    participants = models.ManyToManyField(EmployeeAccount, blank=True)

    class Meta:
        verbose_name = ("Evenement")
        verbose_name_plural = ("Evenements")

    def __str__(self):
        return self.nom