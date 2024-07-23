from django.db import models


# Create your models here.
class Book(models.Model):
    CustomerName = models.CharField(max_length=254)
    CustomerEmail = models.EmailField(max_length=254)
    ContactNumber = models.IntegerField()
    Date = models.DateField()
    

    def __str__(self):
        return self.CustomerName
