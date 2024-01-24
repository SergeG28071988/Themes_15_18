from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Auto
from .forms import AutoForm

# Create your views here.

def auto_list(request):
    cars = Auto.objects.order_by('-id')
    context = {'title': 'Главная страница сайта', 'cars': cars}
    return render(request, 'auto_list.html', context)


def add_auto(request):
    error = ''
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auto_list')
        else:
            error = "Форма была не верной"
    form = AutoForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'add_auto.html', context)


def about(request):
    return render(request, 'about.html')