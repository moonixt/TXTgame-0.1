from django.db import models

# Create your models here.

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30,blank=False,null=False)
    password = models.CharField(max_length=30,blank=False,null=False)

