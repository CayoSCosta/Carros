from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    search = request.GET.get('search')

    try:
        if search:
            cars = Car.objects.filter(model__icontains=search)
        else:
            cars = Car.objects.all()
    except Exception as e:
        return render(request, 'cars.html', {'error': str(e)})
    
    # cars = Car.objects.filter(brand__name='Hyundai') # Fiat
    # cars = Car.objects.filter(model='Palio')21111
    # cars = Car.objects.filter(brand__name__contains='i')
    
    return render(request, 'cars.html', {'cars': cars}) 