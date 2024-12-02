from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroUsuarioForm

def registro_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro exitoso!')
            return redirect('registro')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'usuarios/registro.html', {'form': form})
