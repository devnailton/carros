from django import forms
from cars.models import Car
from django.core.exceptions import ValidationError


    
class CarForm(forms.ModelForm): #A diferença está aqui, herda de ModelForm
    class Meta: #Classe do ModelForm, irei reescrever
        model = Car
        fields = '__all__'

    def clean_value(self): #Nas funções de validação, sempre iniciar com o prefixo clean_ 'nome do campo'
        value = self.cleaned_data.get('value') #Dados limpos e validados (cleaned)
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser R$20.000,00')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 2000:
            self.add_error('factory_year', 'Ano mínimo do carro deve ser 2000')
        return factory_year

    
    def clean_plate(self):
        plate = self.cleaned_data.get('plate')
        car_id = self.instance.id  # Obtém o id do objeto do carro sendo editado

        if car_id is None:
            # Verifica se a placa já está cadastrada se estiver adicionando um novo registro
            if Car.objects.filter(plate=plate).exists():
                raise forms.ValidationError('A placa do carro já está cadastrada')
        return plate
            
