from django.db import models

# Create your models here.
class Sale(models.Model):
    product = models.ForeignKey('api.Product', on_delete=models.CASCADE)  # Assuming Product model is in the `api` app
    quantity_sold = models.IntegerField()
    sale_date = models.DateField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale of {self.product.name} on {self.sale_date}"
