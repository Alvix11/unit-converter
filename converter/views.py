from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import LengthForm
from .utils import length_conversions

# Create your views here.
def length_converter(request):
    
    if request.method == "POST":
        form = LengthForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data["value"]
            from_unit = form.cleaned_data["from_convert"]
            to_unit = form.cleaned_data["to_convert"]
            
            return render(request, "length.html", {
                "result": length_conversions(value, from_unit, to_unit),
                'show_button': False,
                }
            )
    else:
        form = LengthForm()
        
    return render(request, "length.html", {
        "form": form,
        'show_button': True
        }
    ) 

def weight_converter(request):
    return HttpResponse("Esta es la vista de weight_converter")

def temperature_converter(request):
    return HttpResponse("Esta es la vista de temperature_converter")