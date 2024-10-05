from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, RegexValidator

class Inventory(models.Model):
    vehicle_type = models.CharField(max_length=100, validators=[MinLengthValidator(3), RegexValidator ( regex=r'^[a-zA-Z0-9]*$' )],   null= False, blank=False  )
    cost_per_refuel = models.DecimalField(max_digits=20, decimal_places = 2, null=False, blank=False,  validators=[MinValueValidator(0.00)])
    maintenance = models.DecimalField(max_digits =20, decimal_places = 2, null = False, blank = False, default=0, validators=[MinValueValidator(0.00)])
    quantity_in_fleet = models.PositiveIntegerField(null=False, blank=False)
    quantity_in_use = models.PositiveIntegerField(null=False, blank=False)
    total = models.DecimalField(max_digits=20, decimal_places=2, null=False, blank= False)
    entry_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)


    def __str__(self) -> str:
        return self.name 
