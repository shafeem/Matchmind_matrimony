from django.db import models

# Create your models here.


class PersonalityTypes(models.Model):
    TypeId = models.CharField(max_length=50)
    Typename =models.CharField(max_length=100)
    typeshort_name = models.CharField(max_length=50)
    TypeDescription = models.CharField(max_length=200)
    type_image = models.ImageField()
