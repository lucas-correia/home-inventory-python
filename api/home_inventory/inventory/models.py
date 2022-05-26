from pyexpat import model
from xml.etree.ElementInclude import default_loader
from django.db import models

class Shelf(models.Model):
    name = models.CharField(max_length=70,  blank=False, default='')
    position = models.CharField(max_length=100, blank=True, default='')

class Product(models.Model):
    reference = models.CharField(unique=True, max_length=10, blank=False, default='')
    name = models.CharField(unique=True, max_length=70, blank=False, default='')
    shelf_id = models.IntegerField(blank=False)
    good_thru = models.DateField()
    observation = models.CharField(max_length=255, default='')
