from django.db import models


class Scoops(models.Model):
    name = models.CharField(max_length=254)
    category = models.CharField(max_length=254)
    is_vegetarian = models.BooleanField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Scoops"


class Bags(models.Model):
    name = models.CharField(max_length=254)
    category = models.CharField(max_length=254)
    description = models.TextField()
    weight = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Bags"