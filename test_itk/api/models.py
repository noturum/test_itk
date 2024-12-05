from django.db import models

class TableData(models.Model):
    ne = models.CharField(max_length=40)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    gsm = models.BooleanField()
    umts = models.BooleanField()
    lte = models.BooleanField()
    status = models.BooleanField(default=False)
