from django import forms

class LengthForm(forms.Form):
    options = [
        ('km', 'Kilometer'),
        ('m', 'Meter'),
        ('cm', 'Centimeter'),
        ('mm', 'Millimeter'),
        ('ft', 'Foot'),
        ('in', 'Inch'),
        ('yd', 'Yard'),
        ('mi', 'Mile')
    ]
    
    value = forms.FloatField(
        label="Enter the length to convert:",
        required=True,
    )
    
    from_unit = forms.ChoiceField(
        choices=options,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Unit to convert from:",
        required=True,
    )
    
    to_unit = forms.ChoiceField(
        choices=options,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Unit to convert to:",
        required=True,
    )

class WeightForm(forms.Form):
    options = [
        ('kg', 'Kilogram'),
        ('g', 'Gram'),
        ('mg', 'Miligram'),
        ('oz', 'Ounce'),
        ('lb', 'Pound')
    ]
    
    value = forms.FloatField(
        label="Enter the weight to convert:",
        required=True,
    )
    
    from_unit = forms.ChoiceField(
        choices=options,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Unit to convert from:",
        required=True,
    )
    
    to_unit = forms.ChoiceField(
        choices=options,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Unit to convert to:",
        required=True,
    )

class TemperatureForm(forms.Form):
    options = [
        ('C', 'Celsius'),
        ('K', 'Kelvin'),
        ('F', 'Fahrenheit')
    ]
    
    value = forms.FloatField(
        label="Enter the temperature to convert:",
        required=True,
    )
    
    from_unit = forms.ChoiceField(
        choices=options,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Unit to convert from:",
        required=True,
    )
    
    to_unit = forms.ChoiceField(
        choices=options,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Unit to convert to:",
        required=True,
    )