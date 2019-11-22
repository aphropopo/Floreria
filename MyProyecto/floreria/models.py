from django.db import models

class Usuario(models.Model):
    user=models.CharField(max_length=100,primary_key=True)  
    pasw=models.CharField(max_length=12)
    
    def __str__(self):
        return self.user


class Flores(models.Model):
    name=models.CharField(max_length=60,primary_key=True)
    valor=models.IntegerField()
    descripcion=models.TextField()
    stock=models.IntegerField()

    def __str__(self):
        return self.name