# в файле views.py вашего приложения
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def index(request):
    return render(request, 'users/register.html')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users-list')  # Укажите URL для перехода после успешной регистрации
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})


