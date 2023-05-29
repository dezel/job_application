from rest_framework import serializers
from backend.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields =['id','first_name', 'last_name', 'department','active', 'email', 'created']