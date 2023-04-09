from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Slicice(models.Model):
    ime = models.CharField(max_length=64, null=False, unique=True)
    opis = models.TextField(default='', blank=True)
    slika = models.ImageField(upload_to='slicice')
    url = models.CharField(max_length=30)
    kreirano = models.DateTimeField(auto_now_add=True)
    kreirao = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='slicice')

    def __str__(self):
        return f'Aplikacija {self.id} {self.ime}'
    
    class Meta:
        verbose_name_plural = 'moja aplikacija'
        ordering = ['ime']