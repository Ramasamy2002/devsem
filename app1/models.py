from django.db import models

class table1(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    roll=models.DecimalField(max_digits=10,decimal_places=5)
