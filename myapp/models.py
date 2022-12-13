from django.db import models


class Hall(models.Model):
    name = models.CharField('name', 'name', max_length=50)


class Dish(models.Model):
    name = models.CharField('name', 'name', max_length=50)


class Order(models.Model):
    FIO = models.CharField('fio', 'fio', max_length=50)
    DATE = models.DateTimeField('date', 'date')
    HALL = models.ForeignKey(Hall, on_delete=models.CASCADE)
    DISHES = models.ManyToManyField(Dish)
    NUM_PEOPLE = models.IntegerField('num_people', 'num_people')
    IS_DATA_PROC = models.BooleanField('is_data_proc', 'is_data_proc')
