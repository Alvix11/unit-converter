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
        label="Enter the length to convert",
        required=True,
    )
    from_convert = forms.ChoiceField(
        choices=options,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Unit to convert from:",
        required=True,
    )
    to_convert = forms.ChoiceField(
        choices=options,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Unit to convert to",
        required="True"
    )

