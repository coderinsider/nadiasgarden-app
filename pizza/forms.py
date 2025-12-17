from django import forms
from .models import Pizza

# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping1', max_length=100)
#     topping2 = forms.CharField(label='Topping2',max_length=100)
#     CHOICES = (
#         ("small", "Small"),
#         ("medium", "Medium"),
#         ("large", "Large")
#     )
    
#     sizes    = forms.ChoiceField(label="Size", choices=CHOICES)


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {"topping1": "Topping 1", "topping2": "Topping 2"}