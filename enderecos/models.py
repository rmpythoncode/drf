from django.db import models

# Create your models here.


class Endereco(models.Model):
    linha1 = models.CharField(max_length=200)
    linha2 = models.CharField(max_length=200, blank=True, null=True)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)
    
    
    def __str__(self):
        return self.linha1
    
    
    
    