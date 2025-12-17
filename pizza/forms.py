from django import forms
from .models import Pizza, Size

# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping1', max_length=100)
#     topping2 = forms.CharField(label='Topping2',max_length=100)
#     #topping = forms.MultipleChoiceField(choices=[('pep', 'Pepproni'), ('cheese', 'Cheese'), ('olives', 'Olives')], widget=forms.CheckboxSelectMultiple)
#     CHOICES = (
#         ("small", "Small"),
#         ("medium", "Medium"),
#         ("large", "Large")
#     )
    
#     sizes    = forms.ChoiceField(label="Size", choices=CHOICES)


class PizzaForm(forms.ModelForm):

    # image = forms.ImageField()
    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)
    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {"topping1": "Topping 1", "topping2": "Topping 2"}
        # widgets = {'size': forms.CheckboxSelectMultiple}


class MultiplePizzaForm(forms.ModelForm):
    # pass the code
    number = forms.IntegerField(min_value=2, max_value=6)