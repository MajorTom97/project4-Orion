from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    Description = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "News"
        
class Astro(models.Model):
    post = models.CharField(max_lenght=300)