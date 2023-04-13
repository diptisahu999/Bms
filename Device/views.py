from django.shortcuts import render
from Device.models import Bms_bulding_master,Bms_floor_master,Bms_department_master,Bms_sub_area_master,Bms_locker,Bms_device_master
from Device.serializers import Bms_Bulding_master_Serializer,Bms_floor_master_Serializer,Bms_department_master_Serializer,Bms_sub_area_master_Serializer,Bms_locker_Serializer,Bms_Devices_Serializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        tutorials = Bms_bulding_master.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = Bms_Bulding_master_Serializer(tutorials, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": "200", "message": "Login Successfully", "response":tutorials_serializer.data})
        # 'safe=False' for objects serialization
        
        
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
    
        # tutorial_serializer = TutorialSerializer(data=request.data)
        tutorial_serializer = Bms_Bulding_master_Serializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            # if not Tutorial.objects.filter(published=request.POST['published']).
        # if tutorial_serializer==abc:
            tutorial_serializer.save()
            # print(tutorial_serializer.data)
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_bulding_master.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    




@api_view(['GET', 'PUT', 'DELETE'])
def user(request, pk):
    try: 
        tutorial = Bms_bulding_master.objects.get(pk=pk) 
    except Bms_bulding_master.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = Bms_Bulding_master_Serializer(tutorial) 
        return JsonResponse({"data":"true","status_code": "200", "message": "Get data Successfully", "response":tutorial_serializer.data}) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = Bms_Bulding_master_Serializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)



#Bms_floor_master crud

@api_view(['GET', 'POST', 'DELETE'])
def floor_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        tutorials = Bms_floor_master.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = Bms_floor_master_Serializer(tutorials, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": "200", "message": "Login Successfully", "response":tutorials_serializer.data})
        # 'safe=False' for objects serialization
        
        
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
    
        # tutorial_serializer = TutorialSerializer(data=request.data)
        tutorial_serializer = Bms_floor_master_Serializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            # if not Tutorial.objects.filter(published=request.POST['published']).
        # if tutorial_serializer==abc:
            tutorial_serializer.save()
            # print(tutorial_serializer.data)
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_floor_master.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    




@api_view(['GET', 'PUT', 'DELETE'])
def floor_details(request, pk):
    try: 
        tutorial = Bms_floor_master.objects.get(pk=pk) 
    except Bms_floor_master.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = Bms_floor_master_Serializer(tutorial) 
        return JsonResponse({"data":"true","status_code": "200", "message": "Get data Successfully", "response":tutorial_serializer.data}) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = Bms_floor_master_Serializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
    
   #Bms_Deperament_master crud
   
@api_view(['GET', 'POST', 'DELETE'])
def department_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        tutorials = Bms_department_master.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = Bms_department_master_Serializer(tutorials, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": "200", "message": "Login Successfully", "response":tutorials_serializer.data})
        # 'safe=False' for objects serialization
        
        
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
    
        # tutorial_serializer = TutorialSerializer(data=request.data)
        tutorial_serializer = Bms_department_master_Serializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            # if not Tutorial.objects.filter(published=request.POST['published']).
        # if tutorial_serializer==abc:
            tutorial_serializer.save()
            # print(tutorial_serializer.data)
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_department_master.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    




@api_view(['GET', 'PUT', 'DELETE'])
def department(request, pk):
    try: 
        tutorial = Bms_department_master.objects.get(pk=pk) 
    except Bms_department_master.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = Bms_department_master_Serializer(tutorial) 
        return JsonResponse({"data":"true","status_code": "200", "message": "Get data Successfully", "response":tutorial_serializer.data}) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = Bms_department_master_Serializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 
    
    
# Bms_sub_area_master crud


@api_view(['GET', 'POST', 'DELETE'])
def Bms_sub_area_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        tutorials = Bms_sub_area_master.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = Bms_sub_area_master_Serializer(tutorials, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": "200", "message": "Login Successfully", "response":tutorials_serializer.data})
        # 'safe=False' for objects serialization
        
        
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
    
        # tutorial_serializer = TutorialSerializer(data=request.data)
        tutorial_serializer = Bms_sub_area_master_Serializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            # if not Tutorial.objects.filter(published=request.POST['published']).
        # if tutorial_serializer==abc:
            tutorial_serializer.save()
            # print(tutorial_serializer.data)
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_sub_area_master.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    




@api_view(['GET', 'PUT', 'DELETE'])
def Bms_sub_area(request, pk):
    try: 
        tutorial = Bms_sub_area_master.objects.get(pk=pk) 
    except Bms_sub_area_master.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = Bms_sub_area_master_Serializer(tutorial) 
        return JsonResponse({"data":"true","status_code": "200", "message": "Get data Successfully", "response":tutorial_serializer.data}) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = Bms_sub_area_master_Serializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
    
    
# Bms_locker crud
    

@api_view(['GET', 'POST', 'DELETE'])
def Bms_locker_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        tutorials = Bms_locker.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = Bms_locker_Serializer(tutorials, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": "200", "message": "Login Successfully", "response":tutorials_serializer.data})
        # 'safe=False' for objects serialization
        
        
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
    
        # tutorial_serializer = TutorialSerializer(data=request.data)
        tutorial_serializer = Bms_locker_Serializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            # if not Tutorial.objects.filter(published=request.POST['published']).
        # if tutorial_serializer==abc:
            tutorial_serializer.save()
            # print(tutorial_serializer.data)
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_locker.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    




@api_view(['GET', 'PUT', 'DELETE'])
def Bms_locker_list_details(request, pk):
    try: 
        tutorial = Bms_locker.objects.get(pk=pk) 
    except Bms_locker.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tutorial_serializer = Bms_locker_Serializer(tutorial) 
        return JsonResponse({"data":"true","status_code": "200", "message": "Get data Successfully", "response":tutorial_serializer.data}) 
 
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = Bms_locker_Serializer(tutorial, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tutorial.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

# Device API LIST

@api_view(['GET', 'POST', 'PUT','DELETE'])
def Device_list(request):
    if request.method == 'GET':
        # a=int(input('plese enter the password: '))
        tutorials = Bms_device_master.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        
        tutorials_serializer = Bms_Devices_Serializer(tutorials, many=True)
        # return JsonResponse(tutorials_serializer.data, safe=False)
        return Response({"data":"true","status_code": "200", "message": "Login Successfully", "response":tutorials_serializer.data})
        # 'safe=False' for objects serialization
        
        
    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
    
        # tutorial_serializer = TutorialSerializer(data=request.data)
        tutorial_serializer = Bms_Devices_Serializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            # if not Tutorial.objects.filter(published=request.POST['published']).
        # if tutorial_serializer==abc:
            tutorial_serializer.save()
            # print(tutorial_serializer.data)
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Bms_device_master.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)    
    
    elif request.method == 'PUT': 
        tutorial_data = JSONParser().parse(request) 
        tutorial_serializer = Bms_Devices_Serializer(tutorial_data, data=tutorial_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 