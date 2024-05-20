from cars.models import Car
from cars.forms import CarForm
from django.urls import reverse_lazy # type: ignore
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView  # type: ignore


class CarsListview(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')  
        # super para acessar a classe pai - CarsListView
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
            # cars = cars.filter(model__contains=search) Aqui considera Case Sensitive
        return cars
    
    '''def get_queryset(self):
            return Car.objects.all()
    Esse é o padrão da get_queryset, mas precisei sobrescrever '''


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    success_url = '/cars'


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car_update.html'
    '''  success_url = '/cars'
        Esse é padrão da success, mas precisei sobrescrever
    '''
    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars'