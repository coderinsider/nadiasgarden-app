from django.shortcuts import render
from datetime import datetime
from .forms import PizzaForm
# Create your views here.
def home(request):
    dataArray = {'date': datetime.now().strftime("%b %d, %Y %H:%M:%S")}
    return render(request, 'pizza/home.html', dataArray)


def order(request):
    if request.method == "POST":
        filled_from  = PizzaForm(request.POST)
        if filled_from.is_valid():
            note = "Thanks for ordering. Your %s %s and %s  pizza is on its way" %(filled_from.cleaned_data['sizes'],
            filled_from.cleaned_data['topping1'],
            filled_from.cleaned_data['topping2'],)
            newForm = PizzaForm()
            return render(request, 'pizza/order.html', {'pizzaform': newForm, 'note': note})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': form})