from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.status import HTTP_204_NO_CONTENT
from .serializers import EmployeeSerialzier
from .models import Employee


# Create your views here.
@csrf_exempt
def employeelistview(request):
    if request.method=='GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerialzier(employees, many=True)
        return JsonResponse(serializer.data, safe=False)
        
    elif request.method=='POST':
        jsondata=JSONParser().parse(request)
        serializer=EmployeeSerialzier(data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors)

@csrf_exempt
def employeedetailview(request, pk):
    try:
        employee=Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method=='DELETE':
        employee.delete()
        return HttpResponse('Deleted Successfully', status=201, content_type='application/json')

    elif request.method=='GET':
        serializer= EmployeeSerialzier(employee)
        return JsonResponse(serializer.data, safe=False)

    elif request.method=='PUT':
        jsondata=JSONParser().parse(request)
        serializer=EmployeeSerialzier(employee, data=jsondata)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)
                        







