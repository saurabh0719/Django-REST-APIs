from rest_framework import serializers

from .models import Student, Menu, Breakfast, Lunch, Dinner

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('student_id', 'student_name', 'student_email', 'student_password')

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ('item_id', 'item_name', 'item_price')

class BreakfastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Breakfast
        fields = ('day_name', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6')

class LunchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lunch
        fields = ('day_name', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6')

class DinnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dinner
        fields = ('day_name', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6')