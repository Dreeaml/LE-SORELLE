from django import forms


class ProductsSearch(forms.Form):
    search_terms = forms.CharField(required=False)
    min_price = forms.FloatField(required=False, min_value=0.00)
    max_price = forms.FloatField(required=False)