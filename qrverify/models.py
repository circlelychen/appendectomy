# -*- coding: utf-8 -*-
from django.db import models
class Shop(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    #image = models.BinaryField()
