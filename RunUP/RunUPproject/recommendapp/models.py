from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    prod_id = models.CharField(primary_key=True, max_length=10)
    link = models.URLField()
    gender = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    image = models.URLField()

class Similarity(models.Model):
    target_prod = models.ForeignKey(Product, related_name='target_prod',on_delete=models.CASCADE)
    sim_prod = models.ForeignKey(Product, related_name='sim_prod',on_delete=models.CASCADE)
    similarity = models.FloatField()
