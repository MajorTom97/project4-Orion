from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class News(models.Model):
    id_news = models.IntegerField()
    reactions = models.ManyToManyField(User)
    
    class Meta:
        verbose_name_plural = "News"
        
class AstroPost(models.Model):
    post = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.ImageField(upload_to = 'post/')

    def __str__(self):
        return self.post + '|' + str(self.author)

# class Reaction(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    

