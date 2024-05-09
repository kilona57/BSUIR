from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime, date

class StanderUser(User):
    personal_number = models.IntegerField('Персональный номер')
class Manager(StanderUser):
    access = models.CharField('Менеджер', default = 'Manager')

class StuffMember(StanderUser):
    access = models.CharField('Штатный сотрудник', default = 'StuffMember')    
        
class Customer(StanderUser):
    access = models.CharField('Покупатель', default = 'Customer')
    
class Product(models.Model):
    name = models.CharField('Название')
    class_product = models.CharField('Класс')
    workload = models.IntegerField('Загруженность')
    
class Company(models.Model):
    type = models.CharField('Тип')
    adress = models.CharField('Адрес')
    workload = models.IntegerField('Загруженность')
    free_space = models.IntegerField('Свободное место')
    list_product = models.ForeignKey('Список товаров', Product)
    
class Order(models.Model):
    number = models.IntegerField('Номер')
    list_product = models.CharField('Список товаров', Product)
    
class CustomerOrder(Order):
    adress = models.CharField('Адресс')

class Transaction(models.Model):
    sum = models.FloatField('Сумма транзакции')
    time = models.DateTimeField('Дата и время')
    category = models.CharField('Категория бюджета', max_length = 35)
    user = User('Пользователь')

    def ago(self):
        return datetime.now() - self.time

class Budget(models.Model):
    name = models.CharField('Название', max_length = 35)
    limit = models.FloatField('Лимит средств')
    user = User('Пользователь')

    def average_daily(self):
        transactions = Transaction.objects.filter(category=self.name)
        last = Transaction.objects.order_by("-time")[0].time
        first = Transaction.objects.order_by("time")[0].time
        days = last-first
        days = int(str(days).split(',')[0].split(' ')[0])
        total_spent = self.total_spent()
        return round(total_spent/days, 2)

    def saved(self):
        if self.percentage() > 100: return ':('
        daily = self.average_daily()
        return round(self.limit-(30*daily), 2)
    
    def total_spent(self):
        transactions = Transaction.objects.filter(category=self.name)
        return sum(abs(transaction.sum) for transaction in transactions)
    
    def percentage(self):
        return int(self.total_spent()/self.limit*100)

class Income(models.Model):
    name = models.CharField('Название', max_length = 35)
    sum = models.FloatField('Сумма')
    time = models.DateField('Дата начисления')
    user = User('Пользователь')

    def before(self):
        ya = ['2', '3', '4']
        number =  str(self.time - date.today()).split(',')[0].split(' ')[0]
        if number[-1] == '1': days = ' день'
        elif number[-1] in ya: days = ' дня'
        else: days = ' дней'
        return number + days