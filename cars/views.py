from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all()
    # cars = Car.objects.filter(brand__name='Hyundai') # Fiat
    # cars = Car.objects.filter(model='Palio')21111
    # cars = Car.objects.filter(brand__name__contains='i')
    return render(request, 'cars.html', {'cars': cars}) 