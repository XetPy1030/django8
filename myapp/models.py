from django.db import models


class Hall(models.Model):
    name = models.CharField('name', 'name', max_length=50)


class Dish(models.Model):
    name = models.CharField('name', 'name', max_length=50)


class Order(models.Model):
    full_name = models.CharField('full_name', 'full_name', max_length=50)
    date = models.DateField('date', 'date')
    num_people = models.IntegerField('num_people', 'num_people')
    is_data_proc = models.BooleanField('is_data_proc', 'is_data_proc')
    time_of_day = models.CharField('time_of_day', 'time_of_day', max_length=15)

    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish)
