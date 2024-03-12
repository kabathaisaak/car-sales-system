from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Car
from .forms import CarQueryForm



def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request,'authentication/register.html')


def login(request):
    return render(request,'authentication/login.html')


def about(request):
    return render(request, 'about.html')


def update_car(request):
    if request.method == 'POST':
        car_id = request.POST.get('car_id')
        new_price = request.POST.get('new_price')

        car = get_object_or_404(Car, id=car_id)
        car.price = new_price
        car.save()

        return HttpResponse("Car updated successfully!")

    return render(request, 'update_car.html')


def delete_car(request):
    if request.method == 'POST':
        car_id = request.POST.get('car_id_delete')

        car = get_object_or_404(Car, id=car_id)
        car.delete()

        return HttpResponse("Car deleted successfully!")

    return render(request, 'delete_car.html')


def car_specs(request):
    if request.method == 'GET':
        car_id = request.GET.get('car_id_specs')

        car = get_object_or_404(Car, id=car_id)

        return render(request, 'car_specs.html', {'car_specs': car})

    return HttpResponse("Invalid request for car specifications.")


def car_query_view(request):
    if request.method == 'POST':
        form = CarQueryForm(request.POST)
        if form.is_valid():
            make = form.cleaned_data.get('make')
            model = form.cleaned_data.get('model')
            min_year = form.cleaned_data.get('min_year')
            max_year = form.cleaned_data.get('max_year')
            min_price = form.cleaned_data.get('min_price')
            max_price = form.cleaned_data.get('max_price')

            # Query cars based on form data
            cars = Car.objects.filter(
                make__icontains=make,
                model__icontains=model,
                year__gte=min_year,
                year__lte=max_year,
                price__gte=min_price,
                price__lte=max_price
            )

            return render(request, 'car_query_results.html', {'cars': cars, 'form': form})

    else:
        form = CarQueryForm()

    return render(request, 'car_query.html', {'form': form})



def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})