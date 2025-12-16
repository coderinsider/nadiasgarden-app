from django import forms


class PizzaForm(forms.Form):
    topping1 = forms.CharField(label='Topping1', max_length=100)
    topping2 = forms.CharField(label='Topping2',max_length=100)
    CHOICES = (
        ("small", "Small"),
        ("medium", "Medium"),
        ("large", "Large")
    )
    
    sizes    = forms.ChoiceField(label="Size", choices=CHOICES)