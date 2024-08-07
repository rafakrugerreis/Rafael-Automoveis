from django import forms
from cars.models import Brand, Car


# Inserindo o formulário de cadastro dos carros
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    # Inserindo a validação dos campos
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 10000:
            self.add_error('value', 'Valor mínimo deve ser 10.000,00')
            return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Não foi possível cadastrar carros fabricados antes de 1975')
        return factory_year


