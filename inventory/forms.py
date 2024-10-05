

from django.forms import ModelForm
from .models import Inventory

class AddInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['vehicle_type',  'cost_per_refuel', 'maintenance',  'quantity_in_fleet', 'quantity_in_use',  ]

#forms.py 
class UpdateInventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = ['vehicle_type',  'cost_per_refuel', 'maintenance',  'quantity_in_fleet', 'quantity_in_use',  ]