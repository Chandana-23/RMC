from django.db import models

# Create your models here.
class Gallery(models.Model):
    event_name = models.CharField(max_length=150)
    event_img = models.ImageField(upload_to="media")
    
class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=150)
    query = models.TextField()