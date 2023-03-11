from django.db import models
from django.contrib.auth import get_user_model
from static import ORDER_STATUS, USER_ROLE


status = models.PositiveSmallIntegerField(choices=ORDER_STATUS)
User = get_user_model()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    description = models.TextField()
    publisher = models.CharField(max_length=40)
    publication_year = models.IntegerField()
    page_count = models.IntegerField()
    price = models.FloatField()
    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=50)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=12)
    role = models.CharField(choices=USER_ROLE, default='PUBLIC', max_length=8)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.TimeField()
    status = models.CharField(choices=ORDER_STATUS, default='IN PROGRESS', max_length=12)
    amount = models.IntegerField()

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.FloatField()

class OrderLine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()


    
