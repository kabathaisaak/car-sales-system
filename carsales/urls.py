from django.urls import path
from django.contrib import admin
from .views import update_car, delete_car, car_specs
from carsales import views
from .views import car_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car_list', car_list, name='car_list'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('update_car', update_car, name='update_car'),
    path('delete_car/', delete_car, name='delete_car'),
    path('car_specs/', car_specs, name='car_specs'),
]


