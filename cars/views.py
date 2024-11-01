from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from cars.form import CarModelForm
from cars.models import Car
from django.views import View

# Model View aula 065
class CarsView(View):
    def get(self, request):
        search = request.GET.get('search')
        try:
            if search:
                cars = Car.objects.filter(model__icontains=search)
            else:
                cars = Car.objects.all()
        except Exception as e:
            return render(request, 'cars.html', {'error': str(e)})
            
        return render(request, 'cars.html', {'cars': cars}) 
    
class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm()
        return render(request, 'new_car.html', { 'new_car_form': new_car_form} )
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(request, 'new_car.html', {'new_car_forom': new_car_form} )

# @login_required(login_url=reverse_lazy('login'))
# def cars_view(request):
#     search = request.GET.get('search')

#     try:
#         if search:
#             cars = Car.objects.filter(model__icontains=search)
#         else:
#             cars = Car.objects.all()
#     except Exception as e:
#         return render(request, 'cars.html', {'error': str(e)})
    
#     # cars = Car.objects.filter(brand__name='Hyundai') # Fiat
#     # cars = Car.objects.filter(model='Palio')21111
#     # cars = Car.objects.filter(brand__name__contains='i')
    
#     return render(request, 'cars.html', {'cars': cars}) 


# def new_car_view(request):
#     if request.method == 'POST':
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#     else:
#         new_car_form = CarModelForm()
#     return render(request, 'new_car.html', { 'new_car_form': new_car_form} )
    
    