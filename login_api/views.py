from django.shortcuts import render
from rest_framework import viewsets

from .serializers import StudentSerializer, MenuSerializer, BreakfastSerializer, LunchSerializer, DinnerSerializer
from .models import Student, Menu, Breakfast, Lunch, Dinner


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('student_name')
    serializer_class = StudentSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all().order_by('item_name')
    serializer_class = MenuSerializer

class BreakfastViewSet(viewsets.ModelViewSet):
    queryset = Breakfast.objects.all().order_by('day_name')
    serializer_class = BreakfastSerializer

class LunchViewSet(viewsets.ModelViewSet):
    queryset = Lunch.objects.all().order_by('day_name')
    serializer_class = LunchSerializer

class DinnerViewSet(viewsets.ModelViewSet):
    queryset = Dinner.objects.all().order_by('day_name')
    serializer_class = DinnerSerializer