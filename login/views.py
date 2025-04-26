from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Contraseña'}))

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('inicio')
            form.add_error(None, 'Credenciales inválidas')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def inicio_view(request):
    return render(request, 'login/inicio.html')

@login_required
def empleados_view(request):
    return render(request, 'login/empleados.html')

@login_required
def calculo_view(request):
    return render(request, 'login/calculo.html')

@login_required
def historial_view(request):
    return render(request, 'login/historial.html')

@login_required
def anticipos_view(request):
    return render(request, 'login/anticipos.html')

@login_required
def configuracion_view(request):
    return render(request, 'login/configuracion.html')
