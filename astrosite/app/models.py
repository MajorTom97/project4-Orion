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
    
class userSetting(models.Model):
    username = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name