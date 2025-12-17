from django.shortcuts import render
from datetime import datetime
from django.forms import formset_factory
from .forms import PizzaForm, MultiplePizzaForm
# Create your views here.
def home(request):
    dataArray = {'date': datetime.now().strftime("%b %d, %Y %H:%M:%S")}
    return render(request, 'pizza/home.html', dataArray)


def order(request):
    multiple_form = MultiplePizzaForm()
    if request.method == "POST":
        filled_from  = PizzaForm(request.POST)
        if filled_from.is_valid():
            note = "Thanks for ordering. Your %s %s and %s  pizza is on its way" %(filled_from.cleaned_data['size'],
            filled_from.cleaned_data['topping1'],
            filled_from.cleaned_data['topping2'],)
            newForm = PizzaForm()
            return render(request, 'pizza/order.html', {'pizzaform': newForm, 'note': note, 'multiple_form': multiple_form})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': form, 'multiple_form': multiple_form})
    

def pizzas(request):
    number_of_pizzas = 2
    filled_multple_pizza_from = MultiplePizzaForm(request.GET)

    if filled_multple_pizza_from.is_valid():
        number_of_pizzas = filled_multple_pizza_from.cleaned_data['number']
    
    PizzaFormSet = formset_factory(PizzaForm, extra=number_of_pizzas)
    formset = PizzaFormSet()
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
            note = "Pizzas have been ordered"
        else:
            note = "Order was not created, please try again"

        return render(request, 'pizza/pizza.html', {'note': note, 'formset': formset})