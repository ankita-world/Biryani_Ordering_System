from django.db import models


# Create your models here.
class Biryani_Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name


class Biryani(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    biryani_Type = models.ForeignKey(Biryani_Type, on_delete=models.CASCADE)
