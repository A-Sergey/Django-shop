from django import forms

PRODUCT_QUANITY_CHOICES = [(i,str(i)) for i in range(1,21)]

class BasketAddProductForm(forms.Form):
    #quantity = forms.TypedChoiceField(choices=PRODUCT_QUANITY_CHOICES, coerce=int)
    quantity = forms.IntegerField(min_value=0,initial = '')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    