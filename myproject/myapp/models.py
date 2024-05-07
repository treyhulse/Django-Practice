from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    in_stock = models.BooleanField(default=True)

# Gondola Shelving Model
class GondolaShelving(models.Model):
    CONFIGURATION_CHOICES = [
        ('island', 'Island/Gondola (double-sided)'),
        ('wall', 'Wall (single-sided)'),
    ]
    COLOR_CHOICES = [
        ('CHR', 'Chrome'),
        ('PLT', 'Platinum'),
    ]
    PANEL_TYPE_CHOICES = [
        ('pegboard', 'Pegboard'),
        ('solid', 'Solid'),
    ]
    SHELF_TYPE_CHOICES = [
        ('TL', 'Tilt-in'),
        ('DL', 'Drop-in'),
    ]

    configuration = models.CharField(max_length=6, choices=CONFIGURATION_CHOICES)
    color = models.CharField(max_length=3, choices=COLOR_CHOICES)
    side_a_back_panel_type = models.CharField(max_length=8, choices=PANEL_TYPE_CHOICES)
    side_b_back_panel_type = models.CharField(max_length=8, choices=PANEL_TYPE_CHOICES)
    height = models.IntegerField()  # assuming inches as units
    width = models.IntegerField()  # assuming inches as units
    side_a_base_depth = models.IntegerField()
    side_b_base_depth = models.IntegerField()
    upper_shelves_quantity_per_section = models.IntegerField(default=0)
    upper_shelf_type = models.CharField(max_length=2, choices=SHELF_TYPE_CHOICES)
    upper_shelf_depth = models.IntegerField()
    base_height = models.CharField(max_length=2)  # unclear definition, needs validation
    wall_mount_qty = models.CharField(max_length=15)

# Future Model