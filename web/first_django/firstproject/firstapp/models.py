from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	name = models.CharField(max_length=200)
	image = models.URLField()
	price = models.IntegerField()
	description = models.TextField()

class Comment(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

class Favorite(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)