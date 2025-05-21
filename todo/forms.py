from django import forms

class loginForm(forms.Form):
    nombre = forms.CharField(label = "nombre", max_length=150)
    clave = forms.CharField(label = "clave", max_length = 90, widget =forms.PasswordInput)

class registerForm (forms.Form):
    nombre = forms.CharField(label = "nombre", max_length = 150)
    clave = forms.CharField(label = "clave", max_length = 90, widget =forms.PasswordInput)
    email = forms.EmailField(label = "email", max_length=60)
    numTelefono = forms.CharField(label = "numTelefono", max_length = 10)