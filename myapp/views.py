from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from .forms import OrderForm


def form_order(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('home')

    form = OrderForm

    if request.method == 'POST':
        form = OrderForm(request.POST)
        
        if not form.is_valid():
            return render(request, 'myapp/index.html', context={'form': form})

        model = models.Order.objects.create(
            full_name = form.cleaned_data['full_name'],
            date = form.cleaned_data['date'].date(),
            num_people = form.cleaned_data['num_people'],
            is_data_proc = form.cleaned_data['is_data_proc'],
            time_of_day = form.cleaned_data['time_of_day'],
            hall = models.Hall.objects.get(pk=form.cleaned_data['hall'])
        )
        model.save()
        model.dishes.add(
            models.Dish.objects.get(pk=form.cleaned_data['dish1']),
            models.Dish.objects.get(pk=form.cleaned_data['dish2']),
            models.Dish.objects.get(pk=form.cleaned_data['dish3'])
        )
        model.save()

    return render(request, 'myapp/index.html', context={'form': form})


def list_halls(request):
    halls = models.Hall.objects.all()
    halls_text = [i.name for i in halls]

    return HttpResponse('<br>'.join(halls_text))


def list_dishes(request):
    dishes = models.Dish.objects.all()
    dishes_text = [i.name for i in dishes]

    return HttpResponse('<br>'.join(dishes_text))
