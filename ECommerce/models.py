from django.db import models

# Create your models here.
class Machine (models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    product_type=models.CharField(max_length=70, blank=False, default='')
    water_line_compatible=models.BooleanField(default=False)
    size =models.CharField(max_length=70, blank=False, default='')

class Pod(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    product_type=models.CharField(max_length=70, blank=False, default='')
    pack_size = models.IntegerField()
    coffee_flavor =models.CharField(max_length=70, blank=False, default='')