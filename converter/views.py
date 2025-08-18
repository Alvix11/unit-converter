from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import LengthForm

# Create your views here.
def length_converter(request):
    
    units = ('km', 'cm', 'm', 'mm', 'mi', 'yd', 'in', 'ft')
    
    if request.method == "POST":
        form = LengthForm(request.POST)
        if form.is_valid():
            value = form.cleaned_data["value"]
            from_convert = form.cleaned_data["from_convert"].lower()
            to_convert = form.cleaned_data["to_convert"].lower()
            
            print(value)
            print(from_convert)
            print(to_convert)
            
            if from_convert in units and to_convert in units:
                print('correcto')
            else:
                print('incorrecto')
                    
            return render(request, "length.html", {
                "result": value,
                'show_button': False,
                }
            )
    else:
        form = LengthForm()
        
    return render(request, "length.html", {"form": form, 'show_button': True})

def weight_converter(request):
    return HttpResponse("Esta es la vista de weight_converter")

def temperature_converter(request):
    return HttpResponse("Esta es la vista de temperature_converter")