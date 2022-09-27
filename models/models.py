from django.db import models
from brands.models import Brand
# Create your models here.
class Model(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False, verbose_name='Названия модели')
    engine = models.CharField(max_length=1000, blank=True, null=False, verbose_name='Двигатель модели')
    hp = models.IntegerField(blank=True, null=True, verbose_name='лошадинные силы')
    nm = models.IntegerField(blank=True, null=True, verbose_name="мощность")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(max_length=100)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
