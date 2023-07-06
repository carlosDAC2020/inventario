from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    sales_balance = models.IntegerField(default=0)
    inventory_balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name



class Administrator(User):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
