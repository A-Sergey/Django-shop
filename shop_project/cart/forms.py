from django import forms


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=0, initial="")
    update = forms.BooleanField(
        required=False, initial=True, widget=forms.HiddenInput
    )
