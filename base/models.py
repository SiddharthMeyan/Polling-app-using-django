from django.db import models

# Create your models here.
class Polls(models.Model):
    question = models.CharField(max_length=400)
    o1= models.CharField(max_length=40)
    o2= models.CharField(max_length=40)
    o3= models.CharField(max_length=40)
    o4= models.CharField(max_length=40)
    total_votes = models.IntegerField(blank=True,null=True)
    o1_votes = models.IntegerField(default=0)
    o2_votes = models.IntegerField(default=0)
    o3_votes = models.IntegerField(default=0)
    o4_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question
    