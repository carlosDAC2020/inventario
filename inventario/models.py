from django.db import models
from users.models import Company, Administrator

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Providers(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    Units_available = models.IntegerField(default=0)
    price_by_unit = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
class Bill(models.Model):
    description = models.TextField()
    expedition_date = models.DateTimeField(auto_now_add=True)
    administrator = models.ForeignKey(Administrator, on_delete=models.CASCADE, related_name='bills_administrator')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='bills_company')
    total_price = models.IntegerField()

    def __str__(self):
        mensaje = self.expedition_date+" "+self.total_price
        return mensaje
    
class Order(models.Model):

    OPCIONES_CLASIFICACION = [
        ('Venta', 'Venta'),
        ('Surtido', 'Surtido'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    products_units = models.IntegerField()
    total_price = models.IntegerField()
    administrator = models.ForeignKey(Administrator, on_delete=models.CASCADE, related_name='orders_administrator')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='orders_company')
    type = models.CharField(max_length=10, choices=OPCIONES_CLASIFICACION)

    def __str__(self):
        mensaje = self.product.name+" "+self.products_units+" "+self.total_price+" "+self.type
        return mensaje
    
    def type_order(self):
        return self.type=='Venta'