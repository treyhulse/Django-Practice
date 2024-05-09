from django.db import models
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    in_stock = models.BooleanField(default=True)

# Gondola Shelving Model
class GondolaShelving(models.Model):
    CONFIGURATION_CHOICES = [('island', 'Island/Gondola (double-sided)'), ('wall', 'Wall (single-sided)')]
    COLOR_CHOICES = [('CHR', 'Chrome'), ('PLT', 'Platinum')]
    PANEL_TYPE_CHOICES = [('pegboard', 'Pegboard'), ('solid', 'Solid')]
    UPPER_SHELF_QUANTITY = [('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')]
    SHELF_TYPE_CHOICES = [('TL', 'Tilt-in'), ('DL', 'Drop-in')]
    HEIGHT_CHOICES = [('48', '48 inches'), ('54', '54 inches'), ('60', '60 inches'), ('66', '66 inches'), ('72', '72 inches'), ('78', '78 inches'), ('84', '84 inches'), ('90', '90 inches'), ('96', '96 inches')]
    SIDE_A_BASE_WIDTH_CHOICES = [('13', '13 inches'), ('16', '16 inches'), ('19', '19 inches'), ('22', '22 inches'), ('25', '25 inches'), ('28', '28 inches'), ('31', '31 inches')]
    SIDE_B_BASE_WIDTH_CHOICES = [('13', '13 inches'), ('16', '16 inches'), ('19', '19 inches'), ('22', '22 inches'), ('25', '25 inches'), ('28', '28 inches'), ('31', '31 inches')]
    UPPER_SHELF_DEPTH_CHOICES = [('13', '13 inches'), ('16', '16 inches'), ('19', '19 inches'), ('22', '22 inches'), ('25', '25 inches'), ('28', '28 inches'), ('31', '31 inches')]
    BASE_HEIGHT_CHOICES= [('06', '6 inches'), ('LB', 'Low Base')]

    configuration = models.CharField(max_length=10, choices=CONFIGURATION_CHOICES, default='island')
    color = models.CharField(max_length=3, choices=COLOR_CHOICES, default='CHR')
    side_a_back_panel_type = models.CharField(max_length=8, choices=PANEL_TYPE_CHOICES, default='pegboard')
    side_b_back_panel_type = models.CharField(max_length=8, choices=PANEL_TYPE_CHOICES, default='pegboard')
    height = models.CharField(max_length=3, choices=HEIGHT_CHOICES, default='48')
    side_a_base_width = models.CharField(max_length=3, choices=SIDE_A_BASE_WIDTH_CHOICES, default='13')
    side_b_base_width = models.CharField(max_length=3, choices=SIDE_B_BASE_WIDTH_CHOICES, default='13')
    upper_shelf_quantity = models.CharField(max_length=1, choices=UPPER_SHELF_QUANTITY, default='0')
    upper_shelf_type = models.CharField(max_length=2, choices=SHELF_TYPE_CHOICES, default='TL')
    upper_shelf_depth = models.CharField(max_length=3, choices=UPPER_SHELF_DEPTH_CHOICES, default='13')
    base_height = models.CharField(max_length=2, choices=BASE_HEIGHT_CHOICES, default='06')
    date_added = models.DateTimeField(auto_now_add=True)