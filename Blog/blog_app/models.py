from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Thema(models.Model):
    thema = models.CharField()
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
         return self.thema
    
class SubThema(models.Model):
     subthema = models.TextField()
     date = models.DateTimeField(auto_now_add=True)
     thema = models.ForeignKey(Thema,on_delete=models.CASCADE)

     def __str__ (self):
          return f"{self.subthema[:20]} ... continuara "
     
     


    

