from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.PositiveIntegerField(primary_key=True)
    student_name = models.CharField(max_length=60)
    student_email = models.EmailField(max_length=254)
    student_password = models.CharField(max_length=60)
    def __str__(self):
        return self.student_name

class Menu(models.Model):
    item_id = models.PositiveIntegerField(primary_key=True)
    item_name = models.CharField(max_length=50)
    item_price = models.IntegerField()
    def __str__(self):
        return self.item_name

class Breakfast(models.Model):
    day_name = models.CharField(max_length=50, primary_key=True)
    item1 = models.PositiveIntegerField(null=True)
    item2 = models.PositiveIntegerField(null=True)
    item3 = models.PositiveIntegerField(null=True)
    item4 = models.PositiveIntegerField(null=True)
    item5 = models.PositiveIntegerField(null=True)
    item6 = models.PositiveIntegerField(null=True)
    def __str__(self):
        return self.day_name

class Lunch(models.Model):
    day_name = models.CharField(max_length=50, primary_key=True)
    item1 = models.PositiveIntegerField(null=True)
    item2 = models.PositiveIntegerField(null=True)
    item3 = models.PositiveIntegerField(null=True)
    item4 = models.PositiveIntegerField(null=True)
    item5 = models.PositiveIntegerField(null=True)
    item6 = models.PositiveIntegerField(null=True)
    def __str__(self):
        return self.day_name

class Dinner(models.Model):
    day_name = models.CharField(max_length=50, primary_key=True)
    item1 = models.PositiveIntegerField(null=True)
    item2 = models.PositiveIntegerField(null=True)
    item3 = models.PositiveIntegerField(null=True)
    item4 = models.PositiveIntegerField(null=True)
    item5 = models.PositiveIntegerField(null=True)
    item6 = models.PositiveIntegerField(null=True)
    def __str__(self):
        return self.day_name
    