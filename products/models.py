from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=54)
    friendly_name = models.CharField(max_length=54, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    name = models.CharField(max_length=54)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
