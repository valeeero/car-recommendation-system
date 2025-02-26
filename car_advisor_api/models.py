from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    

class Car(models.Model):
    model_name = models.CharField(max_length=100)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField()

    
