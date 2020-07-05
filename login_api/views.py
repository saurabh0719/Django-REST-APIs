from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view


from .serializers import StudentSerializer, MenuSerializer, BreakfastSerializer, LunchSerializer, DinnerSerializer
from .models import Student, Menu, Breakfast, Lunch, Dinner

@api_view(['GET', 'POST'])
def students_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        students_serializer = StudentSerializer(students, many=True)
        return JsonResponse(students_serializer.data, safe=False)
    
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, sid):
    try: 
        student = Student.objects.get(student_id=sid) 
    except Student.DoesNotExist: 
        return JsonResponse({'message': 'The student does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        student_serializer = StudentSerializer(student) 
        return JsonResponse(student_serializer.data) 
 
    elif request.method == 'PUT': 
        student_data = JSONParser().parse(request) 
        student_serializer = StudentSerializer(student, data=student_data) 
        if student_serializer.is_valid(): 
            student_serializer.save() 
            return JsonResponse(student_serializer.data) 
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        student.delete() 
        return JsonResponse({'message': 'Student was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def menu_list(request):
    if request.method == 'GET':
        menu = Menu.objects.all()
        menu_serializer = MenuSerializer(menu, many=True)
        return JsonResponse(menu_serializer.data, safe=False)

    elif request.method == 'POST':
        menu_data = JSONParser().parse(request)
        menu_serializer = MenuSerializer(data=menu_data)
        if menu_serializer.is_valid():
            menu_serializer.save()
            return JsonResponse(menu_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(menu_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def menu_item(request, iid):
    try: 
        item = Menu.objects.get(item_id=iid) 
    except Menu.DoesNotExist: 
        return JsonResponse({'message': 'The menu item does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        item_serializer = MenuSerializer(item) 
        return JsonResponse(item_serializer.data) 
 
    elif request.method == 'PUT': 
        item_data = JSONParser().parse(request) 
        item_serializer = MenuSerializer(item, data=item_data) 
        if item_serializer.is_valid(): 
            item_serializer.save() 
            return JsonResponse(item_serializer.data) 
        return JsonResponse(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        item.delete() 
        return JsonResponse({'message': 'Menu item was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def menu_item_list(request, low, high):
    try:
        items = Menu.objects.filter(item_price__range=(low,high))
    except Menu.DoesNotExist: 
        return JsonResponse({'message': 'Items are not available in this price range'}, status=status.HTTP_404_NOT_FOUND)
    items_serializer = MenuSerializer(items, many=True)
    return JsonResponse(items_serializer.data, safe=False)

