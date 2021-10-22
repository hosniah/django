from django.db import models

# Create your models here.

class Morceau(models.Model):
    titre = models.CharField(max_length=64)
    artiste = models.CharField(max_length=64)

    def __str__(self):
        return '{self.titre} (({self.artiste})'.format(self=self)