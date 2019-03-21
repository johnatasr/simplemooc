from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .forms import RegistroForm

def register(request):
    template_name = 'contas/registro.html'
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('core:home')
    else:
        form = RegistroForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)

