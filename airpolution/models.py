from django.db import models

# Create your models here.


class Polutant(models.Model):
    #id=models.SmallAutoField()
    name = models.CharField(max_length=10, primary_key=True)
    removed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'polutions'

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    Region = models.CharField(max_length=100, default='')
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'countries'

class PolutantEntry(models.Model):
    polutant = models.ForeignKey(Polutant, on_delete=models.CASCADE, related_name='entries')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='entries')
    city = models.CharField(max_length=50, default='', blank=True)
    annual_PM10 = models.IntegerField()
    year = models.IntegerField()
    type = models.CharField(max_length=100, default='', blank=True)
    Temporal_coverage= models.CharField(max_length=100, default='', blank=True)
    Reference= models.CharField(max_length=100, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.polutant.name} {self.year}'
    
    class Meta:
        verbose_name_plural = 'polutant entry'
    


