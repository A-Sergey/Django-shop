from django import forms

class BasketAddProductForm(forms.Form):
    #quantity = forms.TypedChoiceField(choices=PRODUCT_QUANITY_CHOICES, coerce=int)
    quantity = forms.IntegerField(min_value=0,initial = '')
    update = forms.BooleanField(required=False, initial=True, widget=forms.HiddenInput)
    