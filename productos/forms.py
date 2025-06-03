
from django import forms
from .models import Producto, Category


class registerProduc(forms.Form):
    nombProduc = forms.CharField(max_length=130)
    descripcion = forms.CharField(max_length=80)
    Categoria = forms.ModelChoiceField(queryset=Category.objects.all())
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    imgProduc = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(registerProduc, self).__init__(*args, **kwargs)
        self.fields['Categoria'].queryset = Category.objects.all()  # Se carga correctamente al instanciar