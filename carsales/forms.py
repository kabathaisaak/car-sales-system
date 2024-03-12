
from django import forms

class CarQueryForm(forms.Form):
    make = forms.CharField(required=False)
    model = forms.CharField(required=False)
    min_year = forms.IntegerField(required=False)
    max_year = forms.IntegerField(required=False)
    min_price = forms.DecimalField(required=False)
    max_price = forms.DecimalField(required=False)
