from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    model_name = models.CharField(max_length=100)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.model_name


class User(models.Model):
    email = models.EmailField()
    referred_price_range = models.IntegerField()


class UserPreferredBrand(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
