from rest_framework.response import Response
from rest_framework.decorators import api_view
from backend.models import Employee
from .serializers import EmployeeSerializer


@api_view(['GET'])
def getData(response):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addEmployee(request):
    print(request)
    print(bool(request.data['active']))    
    print(request.data)

    request.data['active']= bool(request.data['active'])
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        print('is valid')
        serializer.save()
        
    return Response(serializer.data)

@api_view(['PUT'])
def update(request):
    print(request.data)
    employee = Employee.objects.get(id=request.data['id'])
    print(employee.last_name)
    serializer = EmployeeSerializer(instance=employee, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        print('save success')
        return Response({'message':'success'})

@api_view(['DELETE'])
def delete(request,id):
    print(id)
    # print(request.DELETE['id'])
    delete_employee = Employee.objects.get(id = id)
    delete_employee.delete()
    print(delete_employee)
    # employee_serializer = EmployeeSerializer(request.data)
    
    
    # # employee_delete = Employee.objects.filter(id=request.data['id'])

    # if employee_serializer.is_valid():
    #     # employee_delete.delete()
    #     pass
    return Response({"message":"delete successful"})

