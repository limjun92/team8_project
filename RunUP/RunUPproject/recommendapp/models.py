from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    prod_id = models.CharField(primary_key=True, max_length=10)
    link = models.URLField()
    gender = models.CharField(max_length=10)
    category = models.CharField(max_length=10)
    image = models.URLField()
    brand = models.CharField(max_length=10)
    price = models.CharField(max_length=10)


class Similarity(models.Model):
    target_prod = models.CharField(max_length=10)
    sim_prod = models.CharField(max_length=10)
    similarity = models.FloatField()

    @property
    def target_product(self):
        return Product.objects.get(prod_id=self.target_prod)
    @property
    def sim_product(self):
        return Product.objects.get(prod_id=self.sim_prod)