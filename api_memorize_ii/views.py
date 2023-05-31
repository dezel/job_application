from rest_framework.response import Response
from rest_framework.decorators import api_view
from backend.models import Employee
from .serializers import EmployeeSerializer
from .serializers import ApplicantSerializer
from backend.models import Applicant
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework import views
from django.contrib.auth import login, logout
from . import serializers
from django.views.decorators.csrf import csrf_exempt
import os
import mimetypes
from django.http import FileResponse

@api_view(['GET'])
def getData(response,id):
    permission_classes = (permissions.AllowAny,)
    applicant = Applicant.objects.get(applicant_number=id)
    serializer = ApplicantSerializer(applicant, many=False)
    return Response(serializer.data)



@api_view(['POST'])
def addApplicant(request):
    print(request)
    # print(bool(request.data['active']))    
    print(request.data)

    # request.data['active']= bool(request.data['active'])
    serializer = ApplicantSerializer(data=request.data)
    
    if serializer.is_valid():
        print('is valid')
        serializer.save()
    else:
        print('not valid')
        
    return Response(serializer.data)



@api_view(['PUT'])
def update(request):
    print(request.data)
    employee = Applicant.objects.get(id=request.data['id'])
    print(employee.last_name)
    serializer = ApplicantSerializer(instance=employee, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        print('save success')
        return Response({'message':'success'})



@api_view(['DELETE'])
def delete(request,id):
    permission_classes = (permissions.AllowAny,)
    print(id)
    # print(request.DELETE['id'])
    delete_applicant = Applicant.objects.get(id = id)
    delete_applicant.delete()
    print(delete_applicant)
    # employee_serializer = EmployeeSerializer(request.data)
    
    
    # # employee_delete = Employee.objects.filter(id=request.data['id'])

    # if employee_serializer.is_valid():
    #     # employee_delete.delete()
    #     pass
    return Response({"message":"delete successful"})

@api_view(['POST'])
def download(request, file_name):
    print(type(request.data))
    print(file_name)
    path_to_file = 'media/'+file_name #os.path.realpath(file_name)
    response = FileResponse(open(path_to_file, 'rb'))
    # file_name = request.file_name[5:]
    response['Content-Disposition'] = 'inline; filename=' + file_name
    return response
    
    
class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data, context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)


class LogoutView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        print('reached')
        logout(request)
        return Response(None, status=status.HTTP_202_ACCEPTED)


class ProfileView(generics.RetrieveAPIView):
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user
