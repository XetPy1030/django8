from django import forms
from . import models

def get_halls():
    return [(i.id, i.name) for i in models.Hall.objects.all()]


def get_dishes():
    return [(i.id, i.name) for i in models.Dish.objects.all()]


times_of_day = [
    ['morning', 'утро'],
    ['day', 'день'],
    ['everning', 'вечер']
]


class OrderForm(forms.Form):
    full_name = forms.CharField(label='ФИО')
    date = forms.DateTimeField(label='Дата торжества')
    num_people = forms.IntegerField(label='Количество человек')
    is_data_proc = forms.BooleanField(label='Согласие на обаботку данных')
    time_of_day = forms.ChoiceField(label='Время суток', choices=times_of_day)
    
    hall = forms.ChoiceField(label='Зал', choices=get_halls())
    dish1 = forms.ChoiceField(label='Блюдо 1', choices=get_dishes())
    dish2 = forms.ChoiceField(label='Блюдо 2', choices=get_dishes())
    dish3 = forms.ChoiceField(label='Блюдо 3', choices=get_dishes())