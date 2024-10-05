


from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Inventory
from django.contrib.auth.decorators import login_required
from .forms import AddInventoryForm, UpdateInventoryForm
from django.shortcuts import redirect, reverse
from django.contrib.auth import logout
from django.contrib import messages
from django_pandas.io import read_frame
import plotly
import plotly.express as px
import json


@login_required
def inventory_list(request):
    inventories = Inventory.objects.all()
    context = {
        "title": "Inventory List",
        "inventories" : inventories
    }
    return render(request, "inventory/inventory_list.html", context=context)

@login_required
def per_product_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {
        'inventory': inventory
    }

    return render(request, "inventory/per_product.html", context=context)



@login_required
def add_product(request):
    if request.method == "POST":
        add_form = AddInventoryForm(data=request.POST)
        if add_form.is_valid():
            new_inventory = add_form.save(commit=False)
            new_inventory.total = (float(add_form.cleaned_data['cost_per_refuel']) * float(add_form.cleaned_data['quantity_in_use'])) + (float(add_form.cleaned_data['quantity_in_use']) * float(add_form.cleaned_data['maintenance']))
            #new_inventory.total = float(add_form.cleaned_data['cost_per_refuel']) * float(add_form.cleaned_data['quantity_in_use'])
            new_inventory.save()
            messages.success(request, "Successfully Added a New Vehicle")
            return redirect("/inventory/")  
    else:
        add_form = AddInventoryForm()

    return render(request, "inventory/inventory_add.html", {"form": add_form})

@login_required
def delete_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    inventory.delete()
    messages.success(request, "Vehicle Deleted")
    return redirect("/inventory/")

@login_required
def update_inventory(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        updateForm = UpdateInventoryForm(request.POST, instance=inventory) 
        if updateForm.is_valid():
            inventory.vehicle_type = updateForm.data['vehicle_type']
            inventory.quantity_in_fleet = updateForm.data['quantity_in_fleet']
            inventory.quantity_in_use = updateForm.data['quantity_in_use']
            inventory.maintenance = updateForm.data['maintenance']
            inventory.total = (float(updateForm.cleaned_data['cost_per_refuel']) * float(updateForm.cleaned_data['quantity_in_use'])) + (float(updateForm.cleaned_data['quantity_in_use']) * float(updateForm.cleaned_data['maintenance']))
           #inventory.total = float(inventory.cost_per_refuel) * float(inventory.quantity_in_use)
            inventory.save()
            messages.success(request, "Inventory Updated")
            return redirect("/inventory/")
        

    else:
        updateForm = UpdateInventoryForm(instance=inventory)
    context = {"form":updateForm}
    return render(request, "inventory/inventory_update.html", context=context )




@login_required
def dashboard(request):
    inventories = Inventory.objects.all()

    df = read_frame(inventories)

    total_graph = df.groupby(by="last_update", as_index=False, sort=False)['total'].sum()
    total_graph = px.line(total_graph, x=total_graph.last_update, y= total_graph.total, title="Total Trend")
    total_graph = json.dumps(total_graph, cls=plotly.utils.PlotlyJSONEncoder)


    most_used_df = df.groupby(by="vehicle_type", ).sum().sort_values(by= "quantity_in_use")
    most_used = px.bar(most_used_df, 
                             x = most_used_df.index,
                             y = most_used_df.quantity_in_use,
                             title="Most Used Vehicles "
                           )
    most_used = json.dumps(most_used, cls=plotly.utils.PlotlyJSONEncoder)


    most_in_fleet_df = df.groupby(by="vehicle_type",).sum().sort_values(by= "quantity_in_fleet")
    most_in_fleet = px.pie(most_in_fleet_df,
                               names= most_in_fleet_df.index,
                               values=most_in_fleet_df.quantity_in_fleet,
                               title= "Most Vehicles In Fleet"
                         )
    most_in_fleet = json.dumps(most_in_fleet, cls=plotly.utils.PlotlyJSONEncoder)



    context = {
        "total_graph": total_graph,
        "most_used": most_used,
        "most_in_fleet": most_in_fleet

    }

    return render(request, "inventory/dashboard.html", context=context)



















     
     
def logout(request):
    """
    This method is for loging out
    """
    logout(request)
    redirect (reverse('login'))



    



