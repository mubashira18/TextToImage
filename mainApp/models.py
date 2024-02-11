from django.db import models


class TTI(models.Model):
    text = models.CharField(max_length=500)
    background = models.CharField(max_length=50)
    fontfamily = models.CharField(max_length=50)
